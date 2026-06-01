"""Общие сущности партнёрских складов FBP."""
from typing import Optional

from pydantic import BaseModel, Field


class FbpAddressDetailing(BaseModel):
    """Детализация адреса партнёрского склада FBP.

    Attributes:
        country: Страна
        region: Регион
        city: Город
        street: Улица
        house: Дом
        zipcode: Почтовый индекс
    """

    country: Optional[str] = Field(None, description="Страна.")
    region: Optional[str] = Field(None, description="Регион.")
    city: Optional[str] = Field(None, description="Город.")
    street: Optional[str] = Field(None, description="Улица.")
    house: Optional[str] = Field(None, description="Дом.")
    zipcode: Optional[str] = Field(None, description="Почтовый индекс.")


class FbpWarehouse(BaseModel):
    """Партнёрский склад FBP.

    Attributes:
        id: Идентификатор склада
        name: Название склада
        partner_name: Название партнёра
        address_detailing: Детализация адреса склада
        is_bonded: Признак приписного (бондового) склада
        supply_types: Доступные на складе типы поставок
        timezone_name: Часовой пояс склада
    """

    id: Optional[int] = Field(None, description="Идентификатор склада.")
    name: Optional[str] = Field(None, description="Название склада.")
    partner_name: Optional[str] = Field(None, description="Название партнёра.")
    address_detailing: Optional[FbpAddressDetailing] = Field(
        None, description="Детализация адреса склада."
    )
    is_bonded: Optional[bool] = Field(
        None, description="Признак приписного (бондового) склада."
    )
    supply_types: list[int] = Field(
        default_factory=list, description="Доступные на складе типы поставок."
    )
    timezone_name: Optional[str] = Field(
        None, description="Часовой пояс склада."
    )
