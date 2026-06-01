"""https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscountWithCondition"""
from pydantic import BaseModel, Field

from ...common.enumerations.seller_actions import SellerActionDiscountType


class SellerActionsCreateDiscountWithConditionRequest(BaseModel):
    """Схема запроса на создание акции с механикой «Скидка от суммы заказа».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        discount_type: Тип скидки — в процентах или в валюте
        discount_value: Размер скидки
        min_order_amount: Минимальная сумма заказа для применения скидки
        title: Название акции
    """

    date_start: str = Field(
        ..., description="Дата и время начала акции в формате RFC3339."
    )
    date_end: str = Field(
        ..., description="Дата и время окончания акции в формате RFC3339."
    )
    discount_type: SellerActionDiscountType = Field(
        ..., description="Тип скидки: `PERCENT` — в процентах, `CURRENCY` — в валюте."
    )
    discount_value: float = Field(
        ..., description="Размер скидки."
    )
    min_order_amount: float = Field(
        ..., description="Минимальная сумма заказа для применения скидки."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsCreateDiscountWithConditionResponse(BaseModel):
    """Схема ответа на создание акции с механикой «Скидка от суммы заказа».

    Attributes:
        action_id: Идентификатор созданной акции
    """

    action_id: int = Field(
        ..., description="Идентификатор созданной акции."
    )
