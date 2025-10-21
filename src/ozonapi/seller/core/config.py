from typing import Optional

from pydantic import Field, field_validator, ConfigDict
from pydantic_settings import BaseSettings

class APIConfig(BaseSettings):
    """Конфигурация API клиента для работы с Ozon Seller API.

    Attributes:
        client_id: Идентификатор клиента Ozon (опционально)
        api_key: Авторизационный ключ Ozon Seller API (опционально)
        log_level: Уровень логирования (опционально)
        base_url: Базовый URL API Ozon (опционально)
        max_requests_per_second: Максимальное количество запросов в секунду (опционально, 50 по документации Ozon)
        cleanup_interval: Интервал очистки неиспользуемых ресурсов в секундах (опционально)
        min_instance_ttl: Минимальное время жизни ограничителей запросов для ClientID в секундах (опционально)
        connector_limit: Лимит одновременных соединений для клиента (опционально)
        request_timeout: Таймаут запросов в секундах (опционально)
        max_retries: Максимальное количество повторных попыток для неудачных запросов (опционально)
        retry_min_wait: Минимальная задержка между повторами неудачных запросов в секундах (опционально)
        retry_max_wait: Максимальная задержка между повторами неудачных запросов в секундах (опционально)

    Notes:
        Любой из атрибутов конфигурации можно задать в файле `.env`, расположенном в корне вашего проекта.
        Правило наименования параметров в `.env`: `префикс OZON_SELLER_ + имя параметра в верхнем регистре`.

        Например, для `client_id` строка в файле `.env` примет вид: `OZON_SELLER_CLIENT_ID=1234556`
    """

    client_id: Optional[str] = Field(
        default=None,
        description="Идентификатор клиента Ozon",
    )
    api_key: Optional[str] = Field(
        default=None,
        description="Авторизационный ключ Ozon Seller API",
    )
    log_level: Optional[str] = Field(
        default="DEBUG",
        description="Уровень логирования."
    )
    base_url: str = Field(
        default="https://api-seller.ozon.ru",
        description="Базовый URL API Ozon"
    )
    max_requests_per_second: int = Field(
        default=25,
        ge=1,
        le=50,
        description="Максимальное количество запросов в секунду (50 по документации Ozon)"
    )
    cleanup_interval: float = Field(
        default=300.0,
        gt=0,
        description="Интервал очистки неиспользуемых ресурсов в секундах"
    )
    min_instance_ttl: float = Field(
        default=300.0,
        gt=0,
        description="Минимальное время жизни ограничителей запросов для ClientID в секундах"
    )
    connector_limit: int = Field(
        default=100,
        ge=1,
        description="Лимит одновременных соединений для клиента"
    )
    request_timeout: float = Field(
        default=30.0,
        gt=0,
        description="Таймаут запросов в секундах"
    )
    max_retries: int = Field(
        default=3,
        ge=0,
        le=10,
        description="Максимальное количество повторных попыток для неудачных запросов"
    )
    retry_min_wait: float = Field(
        default=4.0,
        gt=0,
        description="Минимальная задержка между повторами неудачных запросов в секундах"
    )
    retry_max_wait: float = Field(
        default=10.0,
        gt=0,
        description="Максимальная задержка между повторами неудачных запросов в секундах"
    )

    @field_validator("base_url")
    def validate_base_url(cls, v: str) -> str:
        """Валидация базового URL."""
        if not v.startswith(("http://", "https://")):
            raise ValueError("URL должен начинаться с http:// или https://")
        return v.rstrip("/")

    @field_validator("retry_max_wait")
    def validate_retry_times(cls, v: float, info) -> float:
        """Валидация времени повторов."""
        if "retry_min_wait" in info.data and v < info.data["retry_min_wait"]:
            raise ValueError("retry_max_wait должен быть больше или равен retry_min_wait")
        return v

    model_config = ConfigDict(
        env_prefix='OZON_SELLER_',      #type: ignore
        case_sensitive=False,           #type: ignore
        extra='ignore',
    )