"""https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsAdd"""
from pydantic import BaseModel, Field

from ...common.enumerations.localization import CurrencyCode


class SellerActionsProductsAddProduct(BaseModel):
    """Товар для добавления в акцию продавца.

    Attributes:
        sku: SKU товара
        discount_percent: Процент скидки в акции
        currency: Валюта цен
    """

    sku: int = Field(
        ..., description="SKU товара."
    )
    discount_percent: float = Field(
        ..., description="Процент скидки в акции."
    )
    currency: CurrencyCode = Field(
        ..., description="Валюта цен."
    )


class SellerActionsProductsAddRequest(BaseModel):
    """Схема запроса на добавление товаров в акцию продавца.

    Attributes:
        action_id: Идентификатор акции
        products: Список товаров для добавления в акцию
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    products: list[SellerActionsProductsAddProduct] = Field(
        ..., description="Список товаров для добавления в акцию.",
        min_length=1
    )


class SellerActionsProductsAddResponse(BaseModel):
    """Схема ответа на добавление товаров в акцию продавца.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
