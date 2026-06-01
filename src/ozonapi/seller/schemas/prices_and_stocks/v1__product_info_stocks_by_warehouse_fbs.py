"""Схемы метода product_info_stocks_by_warehouse_fbs_v1 (остатки на складах продавца, v1).

Версия v1 устаревшая: канонической является v2 (`product_info_stocks_by_warehouse_fbs`).
Сохранена для совместимости — см. правило коллизии версий в CLAUDE.md.
"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoStocksByWarehouseFBSV1Request(BaseModel):
    """Описывает схему запроса об остатках на складах продавца (FBS и rFBS, API v1).

    Notes:
        • Укажите `sku` и/или `offer_id`.

    Attributes:
        sku: Идентификаторы товаров в системе Ozon — SKU
        offer_id: Идентификаторы товаров в системе продавца — артикулы
    """
    sku: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    offer_id: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца — артикулы."
    )


class ProductInfoStocksByWarehouseFBSV1Item(BaseModel):
    """Данные об остатках определённого товара по схемам FBS и rFBS (API v1).

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца — артикул
        present: Общее количество товара на складе
        product_id: Идентификатор товара в системе Ozon
        reserved: Количество зарезервированных товаров на складе
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    present: Optional[int] = Field(None, description="Общее количество товара на складе.")
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    reserved: Optional[int] = Field(
        None, description="Количество зарезервированных товаров на складе."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class ProductInfoStocksByWarehouseFBSV1Response(BaseModel):
    """Описывает схему ответа об остатках товаров по схемам FBS и rFBS (API v1).

    Attributes:
        result: Массив данных об остатках товаров по схемам FBS и rFBS
    """
    result: Optional[list[ProductInfoStocksByWarehouseFBSV1Item]] = Field(
        None, description="Массив данных об остатках товаров по схемам FBS и rFBS."
    )
