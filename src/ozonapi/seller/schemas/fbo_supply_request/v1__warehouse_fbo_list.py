"""Схемы метода warehouse_fbo_list (поиск точек отгрузки поставки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyCreateType


class WarehouseFboListRequest(BaseModel):
    """Параметры запроса поиска точек отгрузки поставки.

    Attributes:
        filter_by_supply_type: Типы поставки
        search: Поиск по названию склада
    """
    filter_by_supply_type: list[SupplyCreateType] = Field(
        ..., description="Типы поставки."
    )
    search: str = Field(..., description="Поиск по названию склада.")


class WarehouseFboListCoordinate(BaseModel):
    """Координаты склада.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class WarehouseFboListItem(BaseModel):
    """Склад — точка отгрузки поставки.

    Attributes:
        address: Адрес склада
        coordinates: Координаты склада
        name: Название склада
        warehouse_id: Идентификатор склада
        warehouse_type: Тип склада
    """
    address: Optional[str] = Field(
        None, description="Адрес склада."
    )
    coordinates: Optional[WarehouseFboListCoordinate] = Field(
        None, description="Координаты склада."
    )
    name: Optional[str] = Field(
        None, description="Название склада."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада, пункта выдачи или сортировочного центра."
    )
    warehouse_type: Optional[str] = Field(
        None, description="Тип склада."
    )


class WarehouseFboListResponse(BaseModel):
    """Ответ с результатами поиска точек отгрузки поставки.

    Attributes:
        search: Результат поиска складов
    """
    search: Optional[list[WarehouseFboListItem]] = Field(
        None, description="Результат поиска складов."
    )
