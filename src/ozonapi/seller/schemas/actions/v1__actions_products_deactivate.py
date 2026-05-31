"""https://docs.ozon.ru/api/seller/#operation/ActionsProductsDeactivate"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionsProductsChangeResult


class ActionsProductsDeactivateRequest(BaseModel):
    """Схема запроса на удаление товаров из акции.

    Attributes:
        action_id: Идентификатор акции
        product_ids: Список идентификаторов товаров для удаления из акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    product_ids: list[int] = Field(
        ..., description="Список идентификаторов товаров для удаления из акции.",
        min_length=1
    )


class ActionsProductsDeactivateResponse(BaseModel):
    """Схема ответа на удаление товаров из акции.

    Attributes:
        result: Результат удаления товаров из акции
    """

    result: Optional[ActionsProductsChangeResult] = Field(
        None, description="Результат удаления товаров из акции."
    )
