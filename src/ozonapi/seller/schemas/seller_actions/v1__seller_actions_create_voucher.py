"""https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateVoucher"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.seller_actions import (
    SellerActionDiscountType,
    SellerActionVoucherType,
)


class SellerActionsCreateVoucherParameter(BaseModel):
    """Параметры промокода акции «Скидка по промокоду».

    Attributes:
        count_codes: Количество промокодов
        is_private: Является ли промокод приватным
        type: Тип промокода
    """

    count_codes: Optional[int] = Field(
        None, description="Количество промокодов."
    )
    is_private: Optional[bool] = Field(
        None, description="Является ли промокод приватным."
    )
    type: SellerActionVoucherType = Field(
        ..., description="Тип промокода: `ONE`, `MULTIPLE` или `UNIQUE`."
    )


class SellerActionsCreateVoucherRequest(BaseModel):
    """Схема запроса на создание акции с механикой «Скидка по промокоду».

    Attributes:
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        discount_type: Тип скидки — в процентах или в валюте
        discount_value: Размер скидки
        budget: Бюджет акции — при исчерпании акция останавливается
        title: Название акции
        user_ids: Идентификаторы пользователей, которым доступен промокод
        voucher_parameters: Параметры промокода
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
    budget: Optional[int] = Field(
        None, description="Бюджет акции. Если бюджет закончится, акция остановится."
    )
    title: str = Field(
        ..., description="Название акции."
    )
    user_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы пользователей, которым доступен промокод."
    )
    voucher_parameters: SellerActionsCreateVoucherParameter = Field(
        ..., description="Параметры промокода."
    )


class SellerActionsCreateVoucherResponse(BaseModel):
    """Схема ответа на создание акции с механикой «Скидка по промокоду».

    Attributes:
        action_id: Идентификатор созданной акции
    """

    action_id: int = Field(
        ..., description="Идентификатор созданной акции."
    )
