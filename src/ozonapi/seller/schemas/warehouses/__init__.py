"""Описывает модели методов раздела Склады.
https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
"""
__all__ = [
    "WarehouseListResponse",
    "DeliveryMethodListRequest",
    "DeliveryMethodListResponse",
]

from .v1__delivery_method_list import DeliveryMethodListRequest, DeliveryMethodListResponse
from .v1__warehouse_list import WarehouseListResponse