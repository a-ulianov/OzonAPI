"""https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscount"""
from pydantic import BaseModel, Field


class SellerActionsCreateDiscountRequest(BaseModel):
    """Схема запроса на создание акции с механикой «Скидка».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        min_action_percent: Минимальный процент скидки
        title: Название акции
    """

    date_start: str = Field(
        ..., description="Дата и время начала акции в формате RFC3339."
    )
    date_end: str = Field(
        ..., description="Дата и время окончания акции в формате RFC3339."
    )
    min_action_percent: float = Field(
        ..., description="Минимальный процент скидки."
    )
    title: str = Field(
        ..., description="Название акции."
    )


class SellerActionsCreateDiscountResponse(BaseModel):
    """Схема ответа на создание акции с механикой «Скидка».

    Attributes:
        action_id: Идентификатор созданной акции
    """

    action_id: int = Field(
        ..., description="Идентификатор созданной акции."
    )
