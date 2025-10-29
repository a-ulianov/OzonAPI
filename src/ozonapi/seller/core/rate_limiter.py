import asyncio
import time
from typing import Optional, Any
from aiolimiter import AsyncLimiter

from ...infrastructure.logging import ozonapi_logger as logger


class RateLimiterConfig:
    """Конфигурация ограничителя кол-ва запросов."""

    def __init__(
            self,
            max_requests: int = 50,
            time_window: float = 1.0,
    ) -> None:
        self.max_requests = max_requests
        self.time_window = time_window

    def __repr__(self) -> str:
        return f"RateLimiterConfig(max_requests={self.max_requests}, time_window={self.time_window})"


class RateLimiterManager:
    """
    Менеджер для управления ограничителями запросов по client_id.
    Обеспечивает общий лимит запросов для всех экземпляров с одинаковым client_id.
    """

    def __init__(
            self,
            cleanup_interval: float = 300.0,
            min_instance_ttl: float = 300.0,
            instance_logger = logger,
    ) -> None:
        self._rate_limiters: dict[str, AsyncLimiter] = {}
        self._instance_refs: dict[str, set[int]] = {}
        self._configs: dict[str, RateLimiterConfig] = {}
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
            self._logger.debug(f"Менеджер ограничителей общих клиентских запросов запущен")

    async def shutdown(self) -> None:
        """Корректное завершение работы менеджера."""
        self._shutdown = True
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                self._logger.debug("Задача очистки общих ограничителей клиентских запросов отменена")
            self._cleanup_task = None

        self._logger.debug("Менеджер общих ограничителей клиентских запросов остановлен")

    async def get_limiter(self, client_id: str, config: RateLimiterConfig) -> AsyncLimiter:
        """
        Получает ограничитель кол-ва запросов для указанного client_id.

        Args:
            client_id: Идентификатор клиента
            config: Конфигурация ограничителя

        Returns:
            AsyncLimiter: Общий ограничитель для client_id
        """
        async with self._lock:
            if client_id not in self._rate_limiters:
                limiter = AsyncLimiter(config.max_requests, config.time_window)
                self._rate_limiters[client_id] = limiter
                self._configs[client_id] = config
                if client_id not in self._instance_refs:
                    self._instance_refs[client_id] = set()
                if client_id not in self._last_instance_creation:
                    self._last_instance_creation[client_id] = time.monotonic()
                self._logger.debug(f"Инициализирован новый общий ограничитель запросов для ClientID {client_id}: {config}")

            return self._rate_limiters[client_id]

    async def register_instance(self, client_id: str, instance_id: int) -> None:
        """
        Регистрирует экземпляр класса.

        Args:
            client_id: Идентификатор клиента
            instance_id: Уникальный идентификатор экземпляра
        """
        current_time = time.monotonic()
        async with self._lock:
            if client_id not in self._instance_refs:
                self._instance_refs[client_id] = set()
                self._last_instance_creation[client_id] = current_time
            self._instance_refs[client_id].add(instance_id)
            self._logger.debug(f"Зарегистрировано подключение к API {instance_id} для ClientID {client_id}")

    async def unregister_instance(self, client_id: str, instance_id: int) -> None:
        """
        Удаляет регистрацию экземпляра.

        Args:
            client_id: Идентификатор клиента
            instance_id: Уникальный идентификатор экземпляра
        """
        async with self._lock:
            if client_id in self._instance_refs:
                self._instance_refs[client_id].discard(instance_id)
                self._logger.debug(f"Завершено подключения к API {instance_id} для СlientID {client_id}")

    async def _cleanup_unused_limiters(self) -> None:
        """Очистка неиспользуемых ограничителей кол-ва запросов с учетом минимального времени жизни."""
        async with self._lock:
            current_time = time.monotonic()
            clients_to_remove = []

            for client_id, instances in self._instance_refs.items():
                if not instances:
                    last_creation = self._last_instance_creation.get(client_id, 0)
                    time_since_creation = current_time - last_creation

                    # Планируем очистку, если прошло достаточно времени с создания последнего экземпляра
                    if time_since_creation > self._min_instance_ttl:
                        clients_to_remove.append(client_id)

            for client_id in clients_to_remove:
                self._rate_limiters.pop(client_id, None)
                self._configs.pop(client_id, None)
                self._instance_refs.pop(client_id, None)
                self._last_instance_creation.pop(client_id, None)
                self._logger.debug(f"Очищены ресурсы общего ограничителя запросов для ClientID {client_id}")

    async def _cleanup_loop(self) -> None:
        """Фоновая задача для очистки неиспользуемых ограничителей кол-ва запросов."""
        while not self._shutdown:
            try:
                await asyncio.sleep(self._cleanup_interval)
                await self._cleanup_unused_limiters()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self._logger.error(f"Ошибка в cleanup loop: {e}")
                await asyncio.sleep(60)  # Пауза при ошибках

    async def get_active_client_ids(self) -> list[str]:
        """Формирует список активных client_id."""
        async with self._lock:
            return [cid for cid, instances in self._instance_refs.items() if instances]

    async def get_instance_stats(self) -> dict[str, int]:
        """Формирует статистику по экземплярам."""
        async with self._lock:
            return {
                client_id: len(instances)
                for client_id, instances in self._instance_refs.items()
                if instances
            }

    async def get_limiter_stats(self) -> dict[str, dict[str, Any]]:
        """Формирует детальную статистику по ограничителям."""
        current_time = time.monotonic()
        async with self._lock:
            return {
                client_id: {
                    "config": self._configs[client_id],
                    "instances": len(self._instance_refs[client_id]),
                    "limiter": str(self._rate_limiters[client_id]),
                    "last_instance_creation": self._last_instance_creation.get(client_id),
                    "time_since_creation": current_time - self._last_instance_creation.get(client_id, current_time),
                }
                for client_id in self._rate_limiters
            }
