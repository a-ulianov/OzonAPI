"""https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateMultiLevelDiscount"""
from pydantic import BaseModel, Field

from ...common.enumerations.seller_actions import SellerActionDiscountType
from .base import SellerActionDiscountLevel


class SellerActionsCreateMultiLevelDiscountRequest(BaseModel):
    """Схема запроса на создание акции с механикой «Многоуровневая скидка от суммы».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        discount_type: Тип скидки — в процентах или в валюте
        discount_levels: Уровни скидки в зависимости от суммы заказа
        is_legal_entities_segment: Доступна ли акция сегменту юридических лиц
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
    discount_levels: list[SellerActionDiscountLevel] = Field(
        ..., description="Уровни скидки в зависимости от суммы заказа.",
        min_length=1
    )
    is_legal_entities_segment: bool = Field(
        ..., description="Доступна ли акция сегменту юридических лиц."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsCreateMultiLevelDiscountResponse(BaseModel):
    """Схема ответа на создание акции с механикой «Многоуровневая скидка от суммы».

    Attributes:
        action_id: Идентификатор созданной акции
    """

    action_id: int = Field(
        ..., description="Идентификатор созданной акции."
    )
