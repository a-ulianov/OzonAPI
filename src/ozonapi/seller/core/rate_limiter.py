import time
import typing
import weakref
from logging import Logger

from aiolimiter import AsyncLimiter

from .config import APIConfig

if typing.TYPE_CHECKING:
    from .core import APIManager


class InstanceData:
    def __init__(
            self,
            instance: "APIManager",
    ):
        self._client_id: str = instance.client_id
        self._config: APIConfig = instance.config
        self._updated_at: float = time.monotonic()
        self._limiter: AsyncLimiter = AsyncLimiter(self._config.max_requests_per_second, 1)

    def update(self) -> None:
        """Обновляет время последней активности"""
        self._updated_at = time.monotonic()

    @property
    def updated_at(self) -> float:
        """Возвращает время последней активности"""
        return self._updated_at

    @property
    def limiter(self) -> AsyncLimiter:
        """Обеспечивает доступ к ограничителю запросов инстанса."""
        return self._limiter

    @property
    def config(self) -> APIConfig:
        """Обеспечивает доступ к конфигурации инстанса."""
        return self._config

    @property
    def client_id(self) -> str:
        """Обеспечивает доступ к идентификатору клиента инстанса."""
        return self._client_id


class Register:
    def __init__(self):
        self._limiter = AsyncLimiter(APIConfig.model_construct().max_requests_per_second, 1)
        self.data: dict[weakref.ref, InstanceData] = dict()

    @property
    def limiter(self) -> AsyncLimiter:
        return self._limiter


class RateLimiterManager:
    _clients: dict[str, Register] = dict()

    def __init__(self, instance: "APIManager", logger: Logger):
        self._logger = logger
        self._manager = self.get_or_create_client_register(instance)
        self._instance_data = self.get_or_register_instance(instance)
        self._instance_limiter = self._instance_data.limiter
        self._client_limiter = self._manager.limiter

        self.clear_register_by_ttl()

        self._logger.debug(
            f"Установлено ограничение: {self._instance_data.config.max_requests_per_second} rps"
        )


    @classmethod
    def clear_register_by_ttl(cls):
        """Очищает регистры инстансов по ttl."""
        for client_id in tuple(cls._clients.keys()):
            for ref in tuple(cls._clients[client_id].data.keys()):
                # Для уже не существующих инстансов
                if ref() is None:
                    instance_last_update = cls._clients[client_id].data[ref].updated_at
                    instance_config: APIConfig = cls._clients[client_id].data[ref].config
                    # Если с последней активности инстанса прошло больше времени, чем определено конфигом
                    if instance_last_update < time.monotonic() - instance_config.min_instance_ttl:
                        del cls._clients[client_id].data[ref]
                        if not cls._clients[client_id].data:
                            del cls._clients[client_id]
                            break


    @classmethod
    def get_or_create_client_register(cls, instance: "APIManager") -> Register:
        """Формирует и/или возвращает регистр ограничителей запросов по client_id."""
        if instance.client_id not in cls._clients.keys():
            cls._clients[instance.client_id] = Register()

        return cls._clients[instance.client_id]

    @classmethod
    def get_or_register_instance(cls, instance: "APIManager") -> InstanceData:
        """Регистрирует и/или возвращает данные зарегистрированного инстанса API."""
        register = cls.get_or_create_client_register(instance)
        instance_ref = weakref.ref(instance)
        if instance_ref not in register.data.keys():
            register.data[instance_ref] = InstanceData(instance)
        else:
            register.data[instance_ref].update()

        return register.data[instance_ref]

    def instance_update(self) -> None:
        """Обновляет дату последней активности инстанса в регистре."""
        self._instance_data.update()

    @property
    def instance_limiter(self) -> AsyncLimiter:
        """Обеспечивает доступ к ограничителю запросов инстанса."""
        self.instance_update()
        return self._instance_limiter

    @property
    def client_limiter(self) -> AsyncLimiter:
        """Обеспечивает доступ к ограничителю запросов клиента."""
        return self._client_limiter

    @classmethod
    def get_active_client_ids(cls) -> list[str]:
        """Формирует список активных client_id."""
        return [
            client_id for client_id, register in cls._clients.items()
            if any(ref() is not None for ref in register.data.keys())
        ]

    def shutdown(self) -> None:
        """Обеспечивает корректное завершение работы инстанса."""
        self.clear_register_by_ttl()

    def __del__(self) -> None:
        """Очищает регистры от expired-инстансов перед удалением инстанса."""
        self.shutdown()