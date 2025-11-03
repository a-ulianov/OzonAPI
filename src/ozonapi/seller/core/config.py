from typing import Optional

from ...infrastructure import logging

from pydantic import Field, field_validator, ConfigDict, model_validator
from pydantic_settings import BaseSettings

class APIConfig(BaseSettings):
    """Конфигурация API клиента для работы с Ozon Seller API.

    Attributes:
        client_id: Идентификатор клиента Ozon (опционально)
        api_key: Авторизационный ключ Ozon Seller API (опционально)
        token: OAuth-токен Ozon Seller API (https://docs.ozon.com/api/seller/?#tag/OAuth-token)
        base_url: Базовый URL API Ozon (опционально)
        max_requests_per_second: Максимальное количество запросов в секунду (опционально, 50 по документации Ozon)
        cleanup_interval: Интервал очистки неиспользуемых ресурсов в секундах (опционально)
        min_instance_ttl: Минимальное время жизни ограничителей запросов для ClientID в секундах (опционально)
        connector_limit: Лимит одновременных соединений для клиента (опционально)
        request_timeout: Таймаут запросов в секундах (опционально)
        max_retries: Максимальное количество повторных попыток для неудачных запросов (опционально)
        retry_min_wait: Минимальная задержка между повторами неудачных запросов в секундах (опционально)
        retry_max_wait: Максимальная задержка между повторами неудачных запросов в секундах (опционально)

        log_level: Уровень логирования (опционально)
        log_json: Выводить в JSON (опционально)
        log_format: Формат лога (опционально)
        log_use_async: True, чтобы включить асинхронный режим (опционально)
        log_max_queue_size: Максимальный размер очереди (опционально, только для асинхронного режима)
        log_dir: Адрес к дирректирии с логами (опционально)
        log_file: Имя файла логов (опционально)
        log_max_bytes: Максимальный размер файла логов в байтах (опционально)
        log_backup_files_count: Кол-во файлов архивных логов, которые нужно хранить (опционально)

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
    token: Optional[str] = Field(
        default=None,
        description="OAuth-токен Ozon Seller API",
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
        default=5,
        ge=0,
        le=10,
        description="Максимальное количество повторных попыток для неудачных запросов"
    )
    retry_min_wait: float = Field(
        default=2,
        gt=0,
        description="Минимальная задержка между повторами неудачных запросов в секундах"
    )
    retry_max_wait: float = Field(
        default=10.0,
        gt=0,
        description="Максимальная задержка между повторами неудачных запросов в секундах"
    )

    log_level: Optional[str] = Field(
        'ERROR', pattern='^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$',
        description="Уровень логирования."
    )

    log_json: Optional[bool] = Field(
        False, description="Выводить в JSON."
    )
    log_format: Optional[str] = Field(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s', description="Формат лога."
    )
    log_use_async: Optional[bool] = Field(
        True, description='True, чтобы включить асинхронное логирование.'
    )
    log_max_queue_size: Optional[int] = Field(
        10000, description='Размер очереди (только для async mode).'
    )
    log_dir: Optional[str] = Field(
        None, description="Путь к директории с логами."
    )
    log_file: Optional[str] = Field(
        None, description="Название файла логов. Файловое логирование активируется предоставлением имени файла."
    )
    log_max_bytes: Optional[int] = Field(
        10 * 1024 * 1024, description="Максимальный размер лога."
    )
    log_backup_files_count: Optional[int] = Field(
        5, description="Кол-во архивных файлов."
    )
    logger: Optional[logging.Logger] = Field(
        None, description="Корневой логер раздела seller. Поле заполняется системой."
    )
    @model_validator(mode="after")
    def get_logger(self):
        """Назначает корневой логер раздела для сессии, используется для логирования."""
        if self.logger is None:
            self.logger = logging.manager.get_logger("seller")
        return self

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