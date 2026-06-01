"""https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateVoucher"""
from typing import Optional

from pydantic import BaseModel, Field


class SellerActionsUpdateVoucherParameters(BaseModel):
    """Параметры обновления акции с механикой «Скидка по промокоду».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        discount_value: Размер скидки
        budget: Бюджет акции — при исчерпании акция останавливается
        title: Название акции
        user_ids: Идентификаторы пользователей, которым доступен промокод
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
    budget: Optional[int] = Field(
        None, description="Бюджет акции. Если бюджет закончится, акция остановится."
    )
    title: str = Field(
        ..., description="Название акции."
    )
    user_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы пользователей, которым доступен промокод."
    )


class SellerActionsUpdateVoucherRequest(BaseModel):
    """Схема запроса на обновление акции с механикой «Скидка по промокоду».

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Новые параметры акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    action_parameters: SellerActionsUpdateVoucherParameters = Field(
        ..., description="Новые параметры акции."
    )


class SellerActionsUpdateVoucherResponse(BaseModel):
    """Схема ответа на обновление акции с механикой «Скидка по промокоду».

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
