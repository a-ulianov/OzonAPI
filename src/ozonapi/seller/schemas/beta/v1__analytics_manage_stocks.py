"""Схемы метода analytics_manage_stocks (управление остатками, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class AnalyticsManageStocksFilter(BaseModel):
    """Фильтр запроса остатков.

    Attributes:
        skus: Идентификаторы товаров в системе Ozon — SKU
        stock_types: Типы остатков
        warehouse_ids: Идентификаторы складов
    """
    skus: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    stock_types: Optional[list[str]] = Field(None, description="Типы остатков.")
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class AnalyticsManageStocksRequest(BaseModel):
    """Параметры запроса управления остатками.

    Attributes:
        filter: Фильтр запроса
        limit: Количество значений в ответе
        offset: Количество пропускаемых элементов
    """
    filter: Optional[AnalyticsManageStocksFilter] = Field(
        None, description="Фильтр запроса."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    offset: Optional[int] = Field(
        None, description="Количество пропускаемых элементов."
    )


class AnalyticsManageStocksItem(BaseModel):
    """Остатки товара на складе.

    Attributes:
        defect_stock_count: Количество бракованного товара
        expiring_stock_count: Количество товара с истекающим сроком годности
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        sku: Идентификатор товара в системе Ozon — SKU
        valid_stock_count: Количество годного товара
        waitingdocs_stock_count: Количество товара, ожидающего документы
        warehouse_name: Название склада
    """
    defect_stock_count: Optional[int] = Field(
        None, description="Количество бракованного товара."
    )
    expiring_stock_count: Optional[int] = Field(
        None, description="Количество товара с истекающим сроком годности."
    )
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    valid_stock_count: Optional[int] = Field(
        None, description="Количество годного товара."
    )
    waitingdocs_stock_count: Optional[int] = Field(
        None, description="Количество товара, ожидающего документы."
    )
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class AnalyticsManageStocksResponse(BaseModel):
    """Ответ с остатками товаров на складах.

    Attributes:
        items: Список остатков
    """
    items: Optional[list[AnalyticsManageStocksItem]] = Field(
        None, description="Список остатков."
    )
