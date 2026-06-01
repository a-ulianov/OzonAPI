"""Схемы метода warehouse_ozon_list (список складов Ozon, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import WarehouseOZONType


class WarehouseOzonListRequest(BaseModel):
    """Параметры запроса списка складов Ozon.

    Notes:
        • Поле `warehouse_types` обязательно и должно содержать хотя бы один тип.

    Attributes:
        warehouse_types: Типы складов для фильтрации (минимум один)
    """
    warehouse_types: list[WarehouseOZONType] = Field(
        ..., min_length=1, description="Типы складов для фильтрации (минимум один)."
    )


class WarehouseOzonListItem(BaseModel):
    """Склад Ozon.

    Attributes:
        warehouse_id: Идентификатор склада
        name: Название склада
        short_name: Короткое название склада
        address: Адрес склада
        timezone: Часовой пояс склада
        is_active: Признак активности склада
        warehouse_type: Тип склада
        country_iso_numeric: Числовой код страны по ISO
        is_cross_dock: Признак склада кросс-докинга
        is_distribution_center: Признак распределительного центра
        is_edo: Признак поддержки ЭДО
        is_express: Признак склада Express
        is_for_supply: Признак доступности для поставки
    """
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    name: Optional[str] = Field(None, description="Название склада.")
    short_name: Optional[str] = Field(None, description="Короткое название склада.")
    address: Optional[str] = Field(None, description="Адрес склада.")
    timezone: Optional[str] = Field(None, description="Часовой пояс склада.")
    is_active: Optional[bool] = Field(None, description="Признак активности склада.")
    warehouse_type: Optional[str] = Field(None, description="Тип склада.")
    country_iso_numeric: Optional[int] = Field(
        None, description="Числовой код страны по ISO."
    )
    is_cross_dock: Optional[bool] = Field(
        None, description="Признак склада кросс-докинга."
    )
    is_distribution_center: Optional[bool] = Field(
        None, description="Признак распределительного центра."
    )
    is_edo: Optional[bool] = Field(None, description="Признак поддержки ЭДО.")
    is_express: Optional[bool] = Field(None, description="Признак склада Express.")
    is_for_supply: Optional[bool] = Field(
        None, description="Признак доступности для поставки."
    )


class WarehouseOzonListResponse(BaseModel):
    """Ответ со списком складов Ozon.

    Attributes:
        warehouses: Список складов Ozon
    """
    warehouses: Optional[list[WarehouseOzonListItem]] = Field(
        None, description="Список складов Ozon."
    )
