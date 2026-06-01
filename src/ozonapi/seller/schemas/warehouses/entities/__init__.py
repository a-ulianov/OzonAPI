"""Общие сущности раздела Склады."""
__all__ = [
    "WarehouseFBSCoordinates",
    "WarehouseFBSTimeOfDay",
    "WarehouseFBSPointSearch",
    "WarehouseFBSDropOffPoint",
    "WarehouseFBSDropOffTimeslot",
    "WarehouseFBSPickUpTimeslot",
    "WarehouseFBSReturnPointWorkingDay",
    "WarehouseFBSReturnPoint",
    "WarehouseFBSOptions",
    "WarehouseERFBSOperationResponse",
    "WarehouseERFBSHoliday",
    "WarehouseERFBSWorkingDay",
    "WarehouseERFBSTimetable",
    "WarehouseERFBSReturnSettings",
    "WarehouseERFBSDeliveryCosts",
    "WarehouseERFBSDeliveryPolygon",
]

from .warehouse_erfbs import (
    WarehouseERFBSDeliveryCosts,
    WarehouseERFBSDeliveryPolygon,
    WarehouseERFBSHoliday,
    WarehouseERFBSOperationResponse,
    WarehouseERFBSReturnSettings,
    WarehouseERFBSTimetable,
    WarehouseERFBSWorkingDay,
)
from .warehouse_fbs import (
    WarehouseFBSCoordinates,
    WarehouseFBSDropOffPoint,
    WarehouseFBSDropOffTimeslot,
    WarehouseFBSOptions,
    WarehouseFBSPickUpTimeslot,
    WarehouseFBSPointSearch,
    WarehouseFBSReturnPoint,
    WarehouseFBSReturnPointWorkingDay,
    WarehouseFBSTimeOfDay,
)
