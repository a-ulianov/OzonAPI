"""https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscountWithCondition"""
from pydantic import BaseModel, Field


class SellerActionsUpdateDiscountWithConditionParameters(BaseModel):
    """Параметры обновления акции с механикой «Скидка от суммы заказа».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
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
    discount_value: float = Field(
        ..., description="Размер скидки."
    )
    min_order_amount: float = Field(
        ..., description="Минимальная сумма заказа для применения скидки."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsUpdateDiscountWithConditionRequest(BaseModel):
    """Схема запроса на обновление акции с механикой «Скидка от суммы заказа».

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Новые параметры акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    action_parameters: SellerActionsUpdateDiscountWithConditionParameters = Field(
        ..., description="Новые параметры акции."
    )


class SellerActionsUpdateDiscountWithConditionResponse(BaseModel):
    """Схема ответа на обновление акции с механикой «Скидка от суммы заказа».

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
