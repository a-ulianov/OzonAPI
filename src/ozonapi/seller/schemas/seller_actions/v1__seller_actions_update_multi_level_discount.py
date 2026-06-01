"""https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateMultiLevelDiscount"""
from pydantic import BaseModel, Field

from .base import SellerActionDiscountLevel


class SellerActionsUpdateMultiLevelDiscountParameters(BaseModel):
    """Параметры обновления акции с механикой «Многоуровневая скидка от суммы».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
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


class SellerActionsUpdateMultiLevelDiscountRequest(BaseModel):
    """Схема запроса на обновление акции с механикой «Многоуровневая скидка от суммы».

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Новые параметры акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    action_parameters: SellerActionsUpdateMultiLevelDiscountParameters = Field(
        ..., description="Новые параметры акции."
    )


class SellerActionsUpdateMultiLevelDiscountResponse(BaseModel):
    """Схема ответа на обновление акции с механикой «Многоуровневая скидка от суммы».

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
