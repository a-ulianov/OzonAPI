"""Схемы метода warehouse_fbo_seller_list (список складов продавца, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseFboSellerCoordinates(BaseModel):
    """Координаты склада продавца.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class WarehouseFboSellerAddress(BaseModel):
    """Адрес склада продавца.

    Attributes:
        address: Адрес
        city: Город
        coordinates: Координаты
        country_code: Код страны в формате ISO
        macrolocal_cluster_id: Идентификатор макролокального кластера
        region: Регион
        timezone: Часовой пояс
    """
    address: Optional[str] = Field(None, description="Адрес.")
    city: Optional[str] = Field(None, description="Город.")
    coordinates: Optional[WarehouseFboSellerCoordinates] = Field(
        None, description="Координаты."
    )
    country_code: Optional[str] = Field(
        None, description="Код страны в формате ISO."
    )
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    region: Optional[str] = Field(None, description="Регион.")
    timezone: Optional[str] = Field(None, description="Часовой пояс.")


class WarehouseFboSellerContacts(BaseModel):
    """Контакты склада продавца.

    Attributes:
        phone_numbers: Номера телефонов
    """
    phone_numbers: Optional[list[str]] = Field(
        None, description="Номера телефонов."
    )


class WarehouseFboSellerWorkingDay(BaseModel):
    """Рабочий день склада продавца.

    Attributes:
        day: День недели
        time_from_local: Время начала работы
        time_to_local: Время окончания работы
    """
    day: Optional[str] = Field(None, description="День недели.")
    time_from_local: Optional[str] = Field(
        None, description="Время начала работы."
    )
    time_to_local: Optional[str] = Field(
        None, description="Время окончания работы."
    )


class WarehouseFboSellerItem(BaseModel):
    """Склад продавца.

    Attributes:
        address: Адрес склада
        contacts: Контакты склада
        courier_comment: Комментарий для курьера
        is_active: Признак, что склад активен
        is_pickup: Признак, что доступна отгрузка со склада
        seller_warehouse_id: Идентификатор склада продавца
        seller_warehouse_name: Название склада продавца
        working_days: Рабочие дни склада продавца
    """
    address: Optional[WarehouseFboSellerAddress] = Field(
        None, description="Адрес склада."
    )
    contacts: Optional[WarehouseFboSellerContacts] = Field(
        None, description="Контакты склада."
    )
    courier_comment: Optional[str] = Field(
        None, description="Комментарий для курьера."
    )
    is_active: Optional[bool] = Field(
        None, description="Признак, что склад активен."
    )
    is_pickup: Optional[bool] = Field(
        None, description="Признак, что доступна отгрузка со склада."
    )
    seller_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )
    seller_warehouse_name: Optional[str] = Field(
        None, description="Название склада продавца."
    )
    working_days: Optional[list[WarehouseFboSellerWorkingDay]] = Field(
        None, description="Рабочие дни склада продавца."
    )


class WarehouseFboSellerListResponse(BaseModel):
    """Ответ со списком складов продавца.

    Attributes:
        warehouses: Список складов продавца
    """
    warehouses: Optional[list[WarehouseFboSellerItem]] = Field(
        None, description="Список складов продавца."
    )
