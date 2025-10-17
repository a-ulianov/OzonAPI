"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductGetRelatedSKU"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.products import Availability, DeliverySchema


class ProductRelatedSkuGetRequest(BaseModel):
    """Описывает схему запроса для получения единого SKU по старым идентификаторам SKU FBS и SKU FBO.
    В ответе будут все SKU, связанные с переданными.
    Метод может обработать любые SKU, даже скрытые или удалённые.

    Attributes:
        sku: Список SKU (максимум 200)
    """
    sku: list[int] = Field(
        ..., description="Список SKU (максимум 200).",
        max_length=200
    )


class ProductRelatedSkuGetItem(BaseModel):
    """Информация о связанных SKU.

    Attributes:
        availability: Признак доступности товара по SKU
        deleted_at: Дата и время удаления
        product_id: Идентификатор товара в системе продавца
        sku: Идентификатор товара в системе Ozon
    """
    availability: Availability = Field(
        ..., description="Признак доступности товара по SKU.",
    )
    deleted_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время удаления."
    )
    delivery_schema: DeliverySchema = Field(
        ..., description="Схема доставки.",
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — product_id.",
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class ProductRelatedSkuGetError(BaseModel):
    """Информация о возникшей ошибке.

    Attributes:
        code: Код ошибки
        message: Описание ошибки
        sku: SKU, по которому возникла ошибка
    """
    code: str = Field(
        ..., description="Код ошибки.",
    )
    message: str = Field(
        ..., description="Описание ошибки."
    )
    sku: int = Field(
        ..., description="SKU, по которому возникла ошибка."
    )


class ProductRelatedSkuGetResponse(BaseModel):
    """Описывает схему ответа на запрос получения единого SKU по старым идентификаторам SKU FBS и SKU FBO.

    Attributes:
        items: Информация о связанных SKU
        errors: Информация об ошибках
    """
    items: list[ProductRelatedSkuGetItem] = Field(
        default_factory=list, description="Информация о связанных SKU."
    )
    errors: list[ProductRelatedSkuGetError] | None = Field(
        default_factory=list, description="Информация об ошибках."
    )