"""https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsDelete"""
from pydantic import BaseModel, Field


class SellerActionsProductsDeleteRequest(BaseModel):
    """Схема запроса на удаление товаров из акции продавца.

    Attributes:
        action_id: Идентификатор акции
        skus: Список SKU товаров для удаления из акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    skus: list[str] = Field(
        ..., description="Список SKU товаров для удаления из акции.",
        min_length=1
    )


class SellerActionsProductsDeleteResponse(BaseModel):
    """Схема ответа на удаление товаров из акции продавца.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
