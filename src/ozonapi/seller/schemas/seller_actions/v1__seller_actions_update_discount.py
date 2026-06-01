"""https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscount"""
from pydantic import BaseModel, Field


class SellerActionsUpdateDiscountParameters(BaseModel):
    """Параметры обновления акции с механикой «Скидка».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        title: Название акции
    """

    date_start: str = Field(
        ..., description="Дата и время начала акции в формате RFC3339."
    )
    date_end: str = Field(
        ..., description="Дата и время окончания акции в формате RFC3339."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsUpdateDiscountRequest(BaseModel):
    """Схема запроса на обновление акции с механикой «Скидка».

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Новые параметры акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    action_parameters: SellerActionsUpdateDiscountParameters = Field(
        ..., description="Новые параметры акции."
    )


class SellerActionsUpdateDiscountResponse(BaseModel):
    """Схема ответа на обновление акции с механикой «Скидка».

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
