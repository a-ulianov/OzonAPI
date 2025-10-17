from typing import Optional, Any

from pydantic import BaseModel, Field


class BaseAddressee(BaseModel):
    """Контактные данные покупателя/получателя."""
    name: Optional[str] = Field(
        None, description="Имя покупателя."
    )
    phone: Optional[str] = Field(
        None, description="Всегда возвращает пустую строку.."
    )


class BaseDeliveryMethod(BaseModel):
    """Метод доставки."""
    id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    name: str = Field(
        ..., description="Название метода доставки."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class BaseRequestCursor(BaseModel):
    """Базовая схема запроса с курсором."""
    cursor: Optional[str] = Field(
        default_factory=str, description="Указатель для выборки следующего чанка данных."
    )
    limit: int = Field(
        ..., description="Максимальное количество возвращаемых запросом значений.",
    )


class BaseRequestLastId(BaseModel):
    """Базовая схема запроса с last_id."""
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего товара для пагинации."
    )
    limit: int = Field(
        ..., description="Максимальное количество возвращаемых запросом значений.",
    )


class BaseRequestLimit1000(BaseModel):
    """Базовая схема запроса с limit<=1000."""
    limit: Optional[int] = Field(
        1000, description="Максимальное количество товаров в ответе (максимум 1000).",
        ge=1, le=1000
    )


class BaseRequestOffset(BaseModel):
    """Базовая схема запроса с offset."""
    limit: int = Field(
        ..., description="Количество элементов в ответе.",
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class BaseResponseCursor(BaseModel):
    """Базовый класс, описывающий схему ответа с курсором."""
    cursor: str = Field(
        ..., description="Указатель для выборки следующего чанка данных."
    )
    total: int = Field(
        ..., description="Общее количество результатов."
    )


class BaseResponseHasNext(BaseModel):
    """Базовая схема ответа, содержащего атрибут has_next."""
    has_next: bool = Field(
        ..., description="Признак, что в ответе вернулась только часть значений."
    )
    result: list[Any] = Field(
        ..., description="Список результатов."
    )


class BaseResponseLastId(BaseModel):
    """Базовая схема ответа, содержащего атрибут last_id."""
    last_id: str = Field(
        ..., description="Идентификатор последнего значения на странице."
    )
    total: int = Field(
        ..., description="Общее количество товаров в выборке."
    )