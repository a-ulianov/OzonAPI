"""https://docs.ozon.ru/api/seller/#operation/pricing_items-delete"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyProductsDeleteRequest(BaseModel):
    """Схема запроса на удаление товаров из стратегии ценообразования.

    Attributes:
        product_id: Список идентификаторов товаров в системе Ozon
    """

    product_id: list[str] = Field(
        ...,
        description="Список идентификаторов товаров в системе Ozon — product_id.",
    )


class StrategyProductsDeleteResult(BaseModel):
    """Результат удаления товаров из стратегии ценообразования.

    Attributes:
        failed_product_count: Количество товаров с ошибками
    """

    failed_product_count: Optional[int] = Field(
        None,
        description="Количество товаров с ошибками.",
    )


class StrategyProductsDeleteResponse(BaseModel):
    """Схема ответа на запрос удаления товаров из стратегии ценообразования.

    Attributes:
        result: Результат удаления товаров
    """

    result: Optional[StrategyProductsDeleteResult] = Field(
        None,
        description="Результат удаления товаров из стратегии.",
    )
