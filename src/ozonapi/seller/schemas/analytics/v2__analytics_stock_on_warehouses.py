"""Схемы метода analytics_stock_on_warehouses (отчёт по остаткам и товарам, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.analytics import AnalyticsWarehouseType


class AnalyticsStockOnWarehousesRequest(BaseModel):
    """Параметры запроса отчёта по остаткам и товарам на складах.

    Attributes:
        limit: Количество ответов на странице
        offset: Количество пропускаемых элементов
        warehouse_type: Фильтр по типу склада
    """
    limit: int = Field(..., description="Количество ответов на странице.")
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )
    warehouse_type: Optional[AnalyticsWarehouseType] = Field(
        None, description="Фильтр по типу склада."
    )


class AnalyticsStockOnWarehousesRow(BaseModel):
    """Информация о товаре и его остатках на складе.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        item_code: Идентификатор товара в системе продавца — артикул
        item_name: Название товара в системе Ozon
        free_to_sell_amount: Количество товара, доступное к продаже
        promised_amount: Количество товара, указанное в поставках в пути
        reserved_amount: Количество зарезервированного товара
        warehouse_name: Название склада, где находится товар
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    item_code: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    item_name: Optional[str] = Field(
        None, description="Название товара в системе Ozon."
    )
    free_to_sell_amount: Optional[int] = Field(
        None, description="Количество товара, доступное к продаже."
    )
    promised_amount: Optional[int] = Field(
        None, description="Количество товара, указанное в поставках в пути."
    )
    reserved_amount: Optional[int] = Field(
        None, description="Количество зарезервированного товара."
    )
    warehouse_name: Optional[str] = Field(
        None, description="Название склада, где находится товар."
    )


class AnalyticsStockOnWarehousesResult(BaseModel):
    """Содержимое отчёта по остаткам и товарам.

    Attributes:
        rows: Информация о товарах и остатках
    """
    rows: Optional[list[AnalyticsStockOnWarehousesRow]] = Field(
        None, description="Информация о товарах и остатках."
    )


class AnalyticsStockOnWarehousesResponse(BaseModel):
    """Ответ с отчётом по остаткам и товарам на складах.

    Attributes:
        result: Содержимое отчёта
    """
    result: Optional[AnalyticsStockOnWarehousesResult] = Field(
        None, description="Содержимое отчёта."
    )
