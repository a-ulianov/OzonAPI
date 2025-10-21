import asyncio
import sys
from types import TracebackType
from typing import Any, Literal, Optional, ClassVar

import aiohttp
from dotenv import load_dotenv
from loguru import logger
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

logger.remove()
logger.add(
    sys.stderr,
    level=APIConfig().log_level,
    enqueue=True,
)


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

    def __init__(
            self,
            client_id: Optional[str] = None,
            api_key: Optional[str] = None,
            config: Optional[APIConfig] = None
    ) -> None:
        """
        Инициализация клиента API Ozon.

        Args:
            client_id: ID клиента для доступа к API
            api_key: Ключ API для аутентификации
            config: Конфигурация клиента
        """
        self._config = self.load_config(config)
        self._client_id = client_id or self._config.client_id
        self._api_key = api_key or self._config.api_key
        self._instance_id = id(self)
        self._registered = False
        self._closed = False

        if self._client_id is None or self._api_key is None:
            raise ValueError(
                "Не предоставлены авторизационные данные. Проверьте указание client_id и api_key."
            )

        if APIManager._rate_limiter_manager is None:
            APIManager._rate_limiter_manager = RateLimiterManager(
                cleanup_interval=self._config.cleanup_interval
            )
        if APIManager._session_manager is None:
            APIManager._session_manager = SessionManager(
                timeout=self._config.request_timeout,
                connector_limit=self._config.connector_limit
            )
        if APIManager._method_rate_limiter_manager is None:
            APIManager._method_rate_limiter_manager = MethodRateLimiterManager(
                cleanup_interval=self._config.cleanup_interval
            )

        APIManager._instance_count += 1
        self._validate_credentials()
        logger.debug(f"API-клиент инициализирован для ClientID {self._client_id}")

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

    @classmethod
    async def initialize(cls) -> None:
        """Инициализация ресурсов."""
        if not cls._initialized:
            if cls._rate_limiter_manager:
                await cls._rate_limiter_manager.start()
            if cls._method_rate_limiter_manager:
                await cls._method_rate_limiter_manager.start()
            cls._initialized = True
            logger.debug("Выполнена инициализация ресурсов API-менеджера")

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
            logger.debug("Выполнена деинициализация ресурсов API-менеджера")

    def _validate_credentials(self) -> None:
        """Валидация учетных данных."""
        if not self._client_id or not isinstance(self._client_id, str):
            raise ValueError("client_id не должен быть пустой строкой")
        if not self._api_key or not isinstance(self._api_key, str):
            raise ValueError("api_key не должен быть пустой строкой")

        if self._config.max_requests_per_second > 50:
            logger.warning(
                f"Максимальное кол-во запросов в секунду согласно документации Ozon - 50. "
                f"Установлено: {self._config.max_requests_per_second}"
            )

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

        logger.debug(f"Работа API-клиента для ClientID {self._client_id} завершена")

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

    @classmethod
    def get_instance_count(cls) -> int:
        """Получает количество активных экземпляров."""
        return cls._instance_count

    def _create_retry_decorator(self):
        """Создает декоратор повторов на основе конфигурации."""

        def log_retry(retry_state):
            logger.debug(
                f"Попытка {retry_state.attempt_number} совершения запроса для ClientID {self._client_id}"
                f" завершилась исключением: {retry_state.outcome.exception()}"
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
            before_sleep=before_sleep_log(logger, 30),
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

        log_context.update({
            "error_code": code,
            "error_message": message,
            "error_details": details,
        })

        logger.error(f"Ошибка API: {message}", extra=log_context)

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
            api_name: str = "Ozon Seller API",
            api_version: str = "v1",
            endpoint: str = "",
            json: Optional[dict[str, Any]] = None,
            params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Выполняет HTTP-запрос к API Ozon с учетом ограничения запросов.

        Args:
            method: HTTP метод запроса
            api_name: Название API
            api_version: Версия API
            endpoint: Конечная точка API
            json: Данные для отправки в формате JSON
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

        log_context = {
            "api_name": api_name,
            "client_id": self._client_id,
            "method": method,
            "endpoint": endpoint,
            "api_version": api_version,
            "url": url,
            "has_payload": json is not None,
        }

        logger.debug("Отправка запроса к API", extra=log_context)

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
                    self._client_id, self._api_key, self._instance_id
            ) as session:
                async with rate_limiter:
                    try:
                        async with session.request(
                                method, url, json=json, params=params
                        ) as response:
                            data = await response.json()

                            log_context.update({
                                "status_code": response.status,
                                "response_size": len(str(data))
                            })

                            if response.status >= 400:
                                error = self._handle_error_response(response, data, log_context)
                                if error:
                                    raise error

                            logger.debug("Успешный ответ от API", extra=log_context)
                            return data

                    except asyncio.TimeoutError:
                        logger.error("Таймаут запроса к API", extra=log_context)
                        raise APIError(408, "Request timeout")
                    except asyncio.CancelledError:
                        logger.warning("Запрос к API отменен", extra=log_context)
                        raise
                    except (aiohttp.ClientError, ConnectionError, OSError) as e:
                        log_context.update({
                            "error_type": type(e).__name__,
                            "error_message": str(e)
                        })
                        logger.error(
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