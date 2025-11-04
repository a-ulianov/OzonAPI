import asyncio
import hashlib
import json
from logging import Logger
from types import TracebackType
from typing import Any, Literal, Optional, ClassVar

import aiohttp
from dotenv import load_dotenv
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
)

from .config import APIConfig
from .method_rate_limiter import MethodRateLimiterManager
from .rate_limiter import RateLimiterConfig, RateLimiterManager
from .sessions import SessionManager
from .exceptions import (
    APIClientError,
    APIConflictError,
    APIError,
    APIForbiddenError,
    APINotFoundError,
    APIServerError, APITooManyRequestsError,
)

from ...infrastructure import logging
from ...infrastructure.logging import LoggingSettings


class APIManager:
    """
    Базовый класс для работы с API.

    Предоставляет основные методы для взаимодействия с API, включая управление сессией,
    аутентификацию и базовые HTTP-запросы.
    """

    # Общие менеджеры для всех экземпляров класса
    _rate_limiter_manager: ClassVar[Optional[RateLimiterManager]] = None
    _session_manager: ClassVar[Optional[SessionManager]] = None
    _method_rate_limiter_manager: ClassVar[Optional[MethodRateLimiterManager]] = None
    _initialized: ClassVar[bool] = False
    _instance_count: ClassVar[int] = 0

    _class_logger: ClassVar[Logger] = APIConfig().logger

    def __init__(
            self,
            client_id: Optional[str] = None,
            api_key: Optional[str] = None,
            token: Optional[str] = None,
            config: Optional[APIConfig] = None
    ) -> None:
        """
        Инициализация клиента API Ozon.

        Args:
            client_id: ID клиента для доступа к API
            api_key: Ключ API для аутентификации
            token: OAuth-токен Ozon Seller API
            config: Конфигурация клиента
        """
        self._config = self.load_config(config)
        self._client_id = client_id or self._config.client_id
        self._api_key = api_key or self._config.api_key
        self._token = token or self._config.token

        if (self._token is None and (self._api_key is None or self._client_id is None)):
            raise ValueError(
                "Не предоставлены авторизационные данные. Проверьте указание token или client_id и api_key."
            )

        self._instance_id = id(self)
        self._registered = False
        self._closed = False
        self._logging_manager = None
        self._instance_logger: Logger = self._get_instance_logger()

        self._validate_credentials()

        if self._token is not None and self._client_id is None:
            self._client_id = "OAuth {}".format(int(hashlib.sha256(self._token.encode()).hexdigest()[:10], 16) % 10000000)


        if APIManager._rate_limiter_manager is None:
            APIManager._rate_limiter_manager = RateLimiterManager(
                cleanup_interval=self._config.cleanup_interval,
                instance_logger=logging.manager.get_logger(f"seller.rate_limiter")
            )
        if APIManager._session_manager is None:
            APIManager._session_manager = SessionManager(
                timeout=self._config.request_timeout,
                connector_limit=self._config.connector_limit,
                instance_logger=logging.manager.get_logger(f"seller.session")
            )
        if APIManager._method_rate_limiter_manager is None:
            APIManager._method_rate_limiter_manager = MethodRateLimiterManager(
                cleanup_interval=self._config.cleanup_interval,
                instance_logger=logging.manager.get_logger(f"seller.method_rate_limiter")
            )

        APIManager._instance_count += 1
        self.logger.debug(f"API-клиент инициализирован")

    @classmethod
    def load_config(cls, user_config: APIConfig | None = None) -> APIConfig:
        """Создает конфигурацию с загрузкой из .env файла."""
        load_dotenv()
        base_config = APIConfig()

        if user_config is None:
            return base_config
        else:
            return base_config.model_copy(
                update=user_config.model_dump(
                    exclude_unset=True,
                    exclude_defaults=True
                )
            )

    def _get_instance_logger(self) -> Logger:
        """Инициализирует и возвращает настроенный логер для экземпляра.

        Последнее значение `[x]` в домене обозначает порядковый номер активного
        экземпляра менеджера для данного ClientID.
        """

        log_instance_count = 1

        while True:
            self._logging_manager = logging.LoggerManager(
                f"ozonapi.seller.client[{self._client_id}]-[{log_instance_count}]"
            )

            try:
                self._logging_manager.configure(
                    LoggingSettings(
                        LEVEL=self._config.log_level,
                        JSON=self._config.log_json,
                        FORMAT=self._config.log_format,
                        DIR=self._config.log_dir,
                        FILE=self._config.log_file,
                        MAX_BYTES=self._config.log_max_bytes,
                        BACKUP_FILES_COUNT=self._config.log_backup_files_count,
                    )
                )
            except RuntimeError:
                log_instance_count += 1
            else:
                break

        return self._logging_manager.get_logger()

    @classmethod
    async def initialize(cls) -> None:
        """Инициализация ресурсов."""
        if not cls._initialized:
            if cls._rate_limiter_manager:
                await cls._rate_limiter_manager.start()
            if cls._method_rate_limiter_manager:
                await cls._method_rate_limiter_manager.start()
            cls._initialized = True
            cls._class_logger.debug("Выполнена инициализация ресурсов API-менеджера")

    @classmethod
    async def shutdown(cls) -> None:
        """Очистка ресурсов."""
        if cls._initialized:
            if cls._rate_limiter_manager:
                await cls._rate_limiter_manager.shutdown()
            if cls._method_rate_limiter_manager:
                await cls._method_rate_limiter_manager.shutdown()
            if cls._session_manager:
                await cls._session_manager.close_all()
            cls._initialized = False
            cls._class_logger.debug("Выполнена деинициализация ресурсов API-менеджера")

    def _validate_credentials(self) -> None:
        """Валидация учетных данных."""
        if self._token is not None:
            # Валидация для OAuth-токена
            if self._token.startswith("Bearer "):
                self._token = self._token[7:]
            if not self._token or not isinstance(self._token, str):
                raise ValueError("token должен быть непустой строкой")

        elif self._api_key is not None:
            # Валидация для классической авторизации
            if not self._client_id or not isinstance(self._client_id, str):
                raise ValueError("client_id должен быть непустой строкой")
            if not self._api_key or not isinstance(self._api_key, str):
                raise ValueError("api_key должен быть непустой строкой")
        else:
            raise ValueError("Не предоставлены авторизационные данные")

    async def _ensure_registered(self) -> None:
        """Гарантирует регистрацию экземпляра в менеджерах."""
        if self._closed:
            raise RuntimeError(f"Регистрация API-клиента отменена для ClientID {self._client_id}")

        if not self._registered and self._rate_limiter_manager:
            await self._rate_limiter_manager.register_instance(
                self._client_id, self._instance_id
            )
            self._registered = True

    async def __aenter__(self) -> "APIManager":
        """Асинхронный контекстный менеджер."""
        if self._closed:
            raise RuntimeError(f"Невозможно использовать закрытый API-клиент для ClientID {self._client_id}")

        await self.initialize()
        await self._ensure_registered()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        """Очистка ресурсов при выходе из контекста."""
        await self.close()

    async def close(self) -> None:
        if self._closed:
            return

        self._closed = True

        if self._registered and self._rate_limiter_manager:
            await self._rate_limiter_manager.unregister_instance(
                self._client_id, self._instance_id
            )
            self._registered = False

        APIManager._instance_count -= 1

        if APIManager._instance_count == 0:
            if APIManager._session_manager:
                await APIManager._session_manager.close_all()

        self.logger.debug(f"Работа API-клиента завершена")
        self._logging_manager.shutdown()

    @property
    def client_id(self) -> str:
        """ID клиента."""
        return self._client_id

    @property
    def config(self) -> APIConfig:
        """Конфигурация клиента."""
        return self._config

    @property
    def is_closed(self) -> bool:
        """Проверяет закрыт ли клиент."""
        return self._closed

    @property
    def auth_type(self) -> str:
        """Возвращает тип авторизации."""
        return "oauth" if self._token else "api_key"

    @property
    def logger(self):
        """Возвращает логер экземпляра."""
        return self._instance_logger

    @classmethod
    def get_instance_count(cls) -> int:
        """Получает количество активных экземпляров."""
        return cls._instance_count

    def _create_retry_decorator(self):
        """Создает декоратор повторов на основе конфигурации."""

        def log_retry(retry_state):
            self.logger.debug(
                f"Попытка [{retry_state.attempt_number}/{self._config.max_retries}]. Запрос вернул ошибку: {retry_state.outcome.exception()}"
            )

        return retry(
            retry=retry_if_exception_type(
                (
                    # Обрабатываемые механизмом retry ошибки
                    APIServerError,
                    APITooManyRequestsError,
                    asyncio.TimeoutError
                )
            ),
            stop=stop_after_attempt(self._config.max_retries + 1),
            wait=wait_exponential(
                multiplier=1,
                min=self._config.retry_min_wait,
                max=self._config.retry_max_wait
            ),
            # before_sleep=before_sleep_log(self.logger, 30),
            after=log_retry,
            reraise=True,
        )

    @staticmethod
    def _handle_error_response(response, data: dict, log_context: dict) -> Optional[APIError]:
        """
        Обработка ошибочных ответов API.

        Args:
            response: Объект ответа
            data: Данные ответа
            log_context: Контекст для логирования

        Returns:
            APIError или None если ошибка не критическая
        """
        code = data.get("code", response.status)
        message = data.get("message", "Unknown error")
        details = data.get("details", [])

        APIManager._class_logger.warning(f"Ошибка API: {message}")

        error_map = {
            400: APIClientError,
            403: APIForbiddenError,
            404: APINotFoundError,
            409: APIConflictError,
            429: APITooManyRequestsError,
            500: APIServerError,
        }

        exc_class = error_map.get(response.status, APIError)
        return exc_class(code, message, details)

    async def _request(
            self,
            method: Literal["post", "get", "put", "delete"] = "post",
            api_version: str = "v1",
            endpoint: str = "",
            payload: Optional[dict[str, Any]] = None,
            params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Выполняет HTTP-запрос к API Ozon с учетом ограничения запросов.

        Args:
            method: HTTP метод запроса
            api_name: Название API
            api_version: Версия API
            endpoint: Конечная точка API
            payload: Данные для отправки в формате JSON
            params: Query parameters

        Returns:
            Ответ от API в формате JSON

        Raises:
            APIClientError: При ошибках клиента (400)
            APIForbiddenError: При ошибках доступа (403)
            APINotFoundError: При отсутствии ресурса (404)
            APIConflictError: При конфликте данных (409)
            APITooManyRequestsError: При превышении кол-ва запросов (429)
            APIServerError: При ошибках сервера (500)
            APIError: При прочих ошибках
        """
        if self._closed:
            raise RuntimeError("API-клиент остановлен")

        if not self._rate_limiter_manager or not self._session_manager:
            raise RuntimeError("API-клиент не инициализирован")

        url = f"{self._config.base_url}/{api_version}/{endpoint}"

        def get_payload_snippet(p: dict | None) -> str | None:
            """Возвращает сниппет запроса для отладки."""
            if p is None:
                return None

            string = json.dumps(payload)

            return string if len(string) < 200 else string[:200] + "..."

        log_context = {
            "method": method,
            "endpoint": f"{api_version}/{endpoint}",
            "payload": get_payload_snippet(payload),
        }

        self.logger.info(f"Отправка запроса к API: {log_context}")

        await self._ensure_registered()

        limiter_config = RateLimiterConfig(
            max_requests=self._config.max_requests_per_second,
        )
        rate_limiter = await self._rate_limiter_manager.get_limiter(
            self._client_id, limiter_config
        )

        retry_decorator = self._create_retry_decorator()

        async def _execute_request():
            """Выполнение запроса."""
            async with self._session_manager.get_session(
                    client_id=self._client_id,
                    api_key=self._api_key,
                    instance_id=self._instance_id,
                    token=self._token
            ) as session:
                async with rate_limiter:
                    try:
                        async with session.request(
                                method, url, json=payload, params=params
                        ) as response:
                            data = await response.json()

                            log_context.update({
                                "status_code": response.status,
                                "response_size": len(str(data))
                            })

                            log_context_remove_keys = [
                                'method', 'has_payload', 'payload'
                            ]

                            for key in log_context_remove_keys:
                                if key in log_context:
                                    del (log_context[key])

                            if response.status >= 400:
                                error = self._handle_error_response(response, data, log_context)
                                if error:
                                    raise error

                            self.logger.info(f"Получен ответ от API: {log_context}")
                            return data

                    except asyncio.TimeoutError:
                        self.logger.error("Таймаут запроса к API")
                        raise APIError(408, "Request timeout")
                    except asyncio.CancelledError:
                        self.logger.warning("Запрос к API отменен")
                        raise
                    except (aiohttp.ClientError, ConnectionError, OSError) as e:
                        log_context.update({
                            "error_type": type(e).__name__,
                            "error_message": str(e)
                        })
                        self.logger.error(
                            f"Сетевая ошибка при выполнении запроса к API: {str(e)}",
                            extra=log_context
                        )
                        raise APIError(0, f"Network error: {str(e)}")

        _execute_request_retry = retry_decorator(_execute_request)
        return await _execute_request_retry()

    @classmethod
    async def get_active_client_ids(cls) -> list[str]:
        """Возвращает список client_id с активными экземплярами."""
        if cls._rate_limiter_manager:
            return await cls._rate_limiter_manager.get_active_client_ids()
        return list()

    @classmethod
    async def get_rate_limiter_stats(cls) -> dict[str, int]:
        """Возвращает статистику по ограничителям запросов."""
        if cls._rate_limiter_manager:
            return await cls._rate_limiter_manager.get_instance_stats()
        return dict()

    @classmethod
    async def get_detailed_stats(cls) -> dict[str, dict[str, Any]]:
        """Возвращает детальную статистику."""
        if cls._rate_limiter_manager:
            return await cls._rate_limiter_manager.get_limiter_stats()
        return dict()

    @classmethod
    async def get_method_limiter_stats(cls) -> dict[str, dict[str, Any]]:
        """Возвращает статистику по ограничителям методов."""
        if cls._method_rate_limiter_manager:
            return await cls._method_rate_limiter_manager.get_limiter_stats()
        return dict()
