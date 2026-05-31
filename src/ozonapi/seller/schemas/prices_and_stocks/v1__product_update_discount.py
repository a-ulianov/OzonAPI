"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateDiscount"""
from pydantic import BaseModel, Field


class ProductUpdateDiscountRequest(BaseModel):
    """Схема запроса на установку скидки на уценённый товар.

    Attributes:
        discount: Размер скидки — от 3 до 99 процентов
        product_id: Идентификатор товара в системе Ozon — product_id
    """
    discount: int = Field(
        ..., description="Размер скидки: от 3 до 99 процентов.",
        ge=3, le=99
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon — product_id."
    )


class ProductUpdateDiscountResponse(BaseModel):
    """Схема ответа на запрос установки скидки на уценённый товар.

    Attributes:
        result: Результат работы метода (true, если запрос выполнен без ошибок)
    """
    result: bool = Field(
        ..., description="Результат работы метода. true, если запрос выполнен без ошибок."
    )
