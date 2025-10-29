import asyncio
import hashlib
import time
from functools import wraps
from typing import Optional, Any

from aiolimiter import AsyncLimiter
from pydantic import BaseModel, Field

from ...infrastructure.logging import ozonapi_logger as logger


class MethodRateLimitConfig(BaseModel):
    """Конфигурация ограничений для конкретного метода API."""
    limit_requests: int = Field(..., ge=1, description="Максимальное количество запросов в интервал времени")
    interval_seconds: float = Field(..., gt=0, description="Интервал ограничения количества запросов в секундах")
    method_identifier: str = Field(..., description="Уникальный идентификатор вызываемого метода")


class MethodRateLimiterManager:
    """
    Менеджер для управления ограничителями запросов по методам API.
    Обеспечивает раздельные лимиты для каждого метода и client_id.
    """

    def __init__(
            self,
            cleanup_interval: float = 300.0,
            min_instance_ttl: float = 300.0,
            instance_logger=logger
    ) -> None:
        self._rate_limiters: dict[str, AsyncLimiter] = {}
        self._limiter_configs: dict[str, MethodRateLimitConfig] = {}
        self._last_used: dict[str, float] = {}
        self._last_instance_creation: dict[str, float] = {}
        self._lock = asyncio.Lock()
        self._cleanup_task: Optional[asyncio.Task] = None
        self._shutdown = False
        self._cleanup_interval = cleanup_interval
        self._min_instance_ttl = min_instance_ttl
        self._logger = instance_logger

    async def start(self) -> None:
        """Запуск фоновых задач менеджера."""
        if self._cleanup_task is None:
            self._cleanup_task = asyncio.create_task(self._cleanup_loop())
            self._logger.debug("Менеджер ограничителей методов запущен")

    async def shutdown(self) -> None:
        """Корректное завершение работы менеджера."""
        self._shutdown = True
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                self._logger.debug("Задача очистки ограничителей методов отменена")
            self._cleanup_task = None
        self._logger.debug("Менеджер ограничителей методов остановлен")

    @staticmethod
    def _generate_limiter_key(client_id: str, method_identifier: str) -> str:
        """Генерирует уникальный ключ для ограничителя метода."""
        key_data = f"{client_id}:{method_identifier}"
        return hashlib.md5(key_data.encode()).hexdigest()

    async def get_limiter(self, client_id: str, config: MethodRateLimitConfig) -> AsyncLimiter:
        """
        Получает ограничитель для указанного метода и client_id.

        Args:
            client_id: Идентификатор клиента
            config: Конфигурация ограничителя метода

        Returns:
            AsyncLimiter: Ограничитель для метода
        """
        limiter_key = self._generate_limiter_key(client_id, config.method_identifier)
        current_time = time.monotonic()

        async with self._lock:
            if limiter_key not in self._rate_limiters:
                limiter = AsyncLimiter(config.limit_requests, config.interval_seconds)
                self._rate_limiters[limiter_key] = limiter
                self._limiter_configs[limiter_key] = config
                self._last_instance_creation[limiter_key] = current_time
                self._logger.debug(
                    f"Инициализирован ограничитель запросов для метода {config.method_identifier} "
                    f"ClientID {client_id}: {config.limit_requests} запросов в {config.interval_seconds} сек"
                )

            self._last_used[limiter_key] = current_time
            return self._rate_limiters[limiter_key]

    async def _cleanup_unused_limiters(self) -> None:
        """Очистка неиспользуемых ограничителей методов с учетом минимального времени жизни."""
        async with self._lock:
            current_time = time.monotonic()
            limiters_to_remove = []

            for limiter_key in list(self._last_used.keys()):
                last_used = self._last_used[limiter_key]
                last_creation = self._last_instance_creation.get(limiter_key, last_used)
                time_since_creation = current_time - last_creation
                time_since_usage = current_time - last_used

                if (time_since_usage > self._cleanup_interval and
                        time_since_creation > self._min_instance_ttl):
                    limiters_to_remove.append(limiter_key)

            for limiter_key in limiters_to_remove:
                config = self._limiter_configs.pop(limiter_key, None)
                self._rate_limiters.pop(limiter_key, None)
                self._last_used.pop(limiter_key, None)
                self._last_instance_creation.pop(limiter_key, None)
                if config:
                    self._logger.debug(f"Очищен ограничитель для метода {config.method_identifier}")

    async def _cleanup_loop(self) -> None:
        """Фоновая задача для очистки неиспользуемых ограничителей."""
        while not self._shutdown:
            try:
                await asyncio.sleep(self._cleanup_interval)
                await self._cleanup_unused_limiters()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self._logger.error(f"Ошибка в cleanup loop методов: {e}")
                await asyncio.sleep(60)

    async def get_limiter_stats(self) -> dict[str, dict[str, Any]]:
        """Формирует статистику по ограничителям методов."""
        current_time = time.monotonic()
        async with self._lock:
            stats = {}
            for limiter_key in self._rate_limiters:
                config = self._limiter_configs.get(limiter_key)
                last_used = self._last_used.get(limiter_key, current_time)
                last_creation = self._last_instance_creation.get(limiter_key, current_time)

                if config:
                    stats[limiter_key] = {
                        "config": config,
                        "last_used": last_used,
                        "last_instance_creation": last_creation,
                        "time_since_creation": current_time - last_creation,
                        "time_since_usage": current_time - last_used,
                    }
            return stats


def method_rate_limit(limit_requests: int, interval_seconds: float):
    """
    Декоратор для применения дополнительных ограничений частоты запросов к методам API.

    Args:
        limit_requests: Максимальное количество запросов в указанный интервал
        interval_seconds: Временной интервал в секундах

    Returns:
        Декоратор метода
    """

    def decorator(method):
        # Генерируем уникальный идентификатор метода
        method_identifier = f"{method.__module__}.{method.__qualname__}"
        config = MethodRateLimitConfig(
            limit_requests=limit_requests,
            interval_seconds=interval_seconds,
            method_identifier=method_identifier
        )

        @wraps(method)
        async def wrapper(self, *args, **kwargs):
            _logger = self.logger if hasattr(self, '_logger') else logger
            # Проверяем, что экземпляр имеет необходимые атрибуты
            if not hasattr(self, '_client_id') or not hasattr(self, '_method_rate_limiter_manager'):
                _logger.warning(
                    f"Метод {method_identifier} вызван без инициализации ограничителей. "
                    "Ограничения не применяются."
                )
                return await method(self, *args, **kwargs)

            # Дополнительная проверка, что менеджер не None
            if self._method_rate_limiter_manager is None:
                _logger.warning(
                    f"Менеджер ограничителей методов не инициализирован для {method_identifier}. "
                    "Ограничения не применяются."
                )
                return await method(self, *args, **kwargs)

            # Получаем ограничитель запросов для этого метода
            method_limiter = await self._method_rate_limiter_manager.get_limiter(
                self._client_id, config
            )

            # Применяем ограничитель запросов
            async with method_limiter:
                _logger.debug(
                    f"Применен ограничитель метода {method_identifier} для ClientID {self._client_id}: "
                    f"{limit_requests} запросов в {interval_seconds} сек"
                )
                return await method(self, *args, **kwargs)

        # Добавляем метаданные
        wrapper._rate_limit_config = config
        return wrapper

    return decorator
