"""Схемы метода analytics_turnover_stocks (оборачиваемость товара, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class AnalyticsTurnoverStocksRequest(BaseModel):
    """Параметры запроса оборачиваемости товаров.

    Attributes:
        limit: Количество значений в ответе
        offset: Количество пропускаемых элементов
        sku: Идентификаторы товаров в системе Ozon — SKU
    """
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )
    sku: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class AnalyticsTurnoverStocksItem(BaseModel):
    """Информация об оборачиваемости товара.

    Notes:
        • Поля `idc_grade` и `turnover_grade` принимают значения вида `GRADES_NONE`,
          `GRADES_NOSALES`, `GRADES_GREEN`, `GRADES_YELLOW`, `GRADES_RED`, `GRADES_CRITICAL`;
          типизированы как `str` на случай появления новых значений.

    Attributes:
        ads: Среднесуточное количество проданных единиц товара
        current_stock: Остаток товара, шт.
        idc: На сколько дней хватит остатка товара
        idc_grade: Уровень остатка товара
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        sku: Идентификатор товара в системе Ozon — SKU
        turnover: Фактическая оборачиваемость товара в днях
        turnover_grade: Уровень оборачиваемости товара
    """
    ads: Optional[float] = Field(
        None, description="Среднесуточное количество проданных единиц товара."
    )
    current_stock: Optional[int] = Field(
        None, description="Остаток товара, шт."
    )
    idc: Optional[float] = Field(
        None, description="На сколько дней хватит остатка товара."
    )
    idc_grade: Optional[str] = Field(
        None, description="Уровень остатка товара."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    turnover: Optional[float] = Field(
        None, description="Фактическая оборачиваемость товара в днях."
    )
    turnover_grade: Optional[str] = Field(
        None, description="Уровень оборачиваемости товара."
    )


class AnalyticsTurnoverStocksResponse(BaseModel):
    """Ответ с оборачиваемостью товаров.

    Attributes:
        items: Товары
    """
    items: Optional[list[AnalyticsTurnoverStocksItem]] = Field(
        None, description="Товары."
    )
