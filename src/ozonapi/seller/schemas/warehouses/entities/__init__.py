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
]

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
