"""Описывает модели методов раздела Склады.
https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
"""
__all__ = [
    "WarehouseListRequest",
    "WarehouseListResponse",
    "WarehouseListItem",
    "WarehouseListAddressInfo",
    "WarehouseListFirstMile",
    "WarehouseListTimetable",
    "WarehouseListWorkingHours",
    "DeliveryMethodListRequest",
    "DeliveryMethodListResponse",
    "DeliveryMethodListFilter",
    "DeliveryMethodListItem",
    "DeliveryMethodListDropOffPoint",
    "DeliveryMethodListAddressCoordinates",
]

from .v2__delivery_method_list import (
    DeliveryMethodListRequest,
    DeliveryMethodListResponse,
    DeliveryMethodListFilter,
    DeliveryMethodListItem,
    DeliveryMethodListDropOffPoint,
    DeliveryMethodListAddressCoordinates,
)
from .v2__warehouse_list import (
    WarehouseListRequest,
    WarehouseListResponse,
    WarehouseListItem,
    WarehouseListAddressInfo,
    WarehouseListFirstMile,
    WarehouseListTimetable,
    WarehouseListWorkingHours,
)
