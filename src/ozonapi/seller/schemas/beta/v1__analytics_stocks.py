"""https://docs.ozon.com/api/seller/#operation/AnalyticsAPI_AnalyticsStocks"""
from typing import Optional
from pydantic import BaseModel, Field

from ...common.enumerations.products import TurnoverGrade, ItemTag


class AnalyticsStocksRequest(BaseModel):
    """Схема запроса для получения аналитики по остаткам.

    Attributes:
        cluster_ids: Фильтр по идентификаторам кластеров
        item_tags: Фильтр по тегам товара
        skus: Фильтр по идентификаторам товаров в системе Ozon — SKU
        turnover_grades: Фильтр по статусу ликвидности товаров
        warehouse_ids: Фильтр по идентификаторам складов
    """
    cluster_ids: Optional[list[int]] = Field(
        None, description="Фильтр по идентификаторам кластеров. Получить идентификаторы можно через метод cluster_list()."
    )
    item_tags: Optional[list[ItemTag]] = Field(
        None, description="Фильтр по тегам товара."
    )
    skus: list[int] = Field(
        ..., description="Фильтр по идентификаторам товаров в системе Ozon — SKU.",
        min_length=1, max_length=100
    )
    turnover_grades: Optional[list[TurnoverGrade]] = Field(
        None, description="Фильтр по статусу ликвидности товаров."
    )
    warehouse_ids: Optional[list[int]] = Field(
        None, description="Фильтр по идентификаторам складов. Получить идентификаторы можно через метод warehouse_list()."
    )


class AnalyticsStocksItem(BaseModel):
    """Схема для элемента аналитики по остаткам.

    Attributes:
        ads: Среднесуточное количество проданных единиц товара за последние 28 дней по всем кластерам
        ads_cluster: Среднесуточное количество проданных единиц товара за последние 28 дней в кластере
        available_stock_count: Количество товаров, которые доступны к продаже
        cluster_id: Идентификатор кластера
        cluster_name: Название кластера
        days_without_sales: Количество дней без продаж по всем кластерам
        days_without_sales_cluster: Количество дней без продаж в кластере
        excess_stock_count: Количество излишков с поставки, которые доступны к вывозу
        expiring_stock_count: Количество единиц товара с истекающим сроком годности
        idc: Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней по всем кластерам
        idc_cluster: Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней в кластере
        item_tags: Теги товара
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        other_stock_count: Количество единиц товара, проходящих проверку
        requested_stock_count: Количество единиц товара в заявках на поставку
        return_from_customer_stock_count: Количество единиц товара в процессе возврата от покупателей
        return_to_seller_stock_count: Количество единиц товара, готовящихся к вывозу по вашей заявке
        sku: Идентификатор товара в системе Ozon — SKU
        stock_defect_stock_count: Количество брака, доступное к вывозу со стока
        transit_defect_stock_count: Количество брака, доступное к вывозу с поставки
        transit_stock_count: Количество единиц товара в поставках в пути
        turnover_grade: Статус ликвидности товара по всем кластерам
        turnover_grade_cluster: Статус ликвидности товара в кластере
        valid_stock_count: Количество товаров, которые готовятся к продаже
        waiting_docs_stock_count: Количество маркируемых товаров, которые ожидают ваших действий
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    ads: float = Field(
        ..., description="Среднесуточное количество проданных единиц товара за последние 28 дней по всем кластерам."
    )
    ads_cluster: float = Field(
        ..., description="Среднесуточное количество проданных единиц товара за последние 28 дней в кластере."
    )
    available_stock_count: int = Field(
        ..., description="Количество товаров, которые доступны к продаже. Соответствует столбцу «Доступно к продаже»."
    )
    cluster_id: int = Field(
        ..., description="Идентификатор кластера. Получить подробную информацию о кластере можно через метод cluster_list()."
    )
    cluster_name: str = Field(
        ..., description="Название кластера."
    )
    days_without_sales: int = Field(
        ..., description="Количество дней без продаж по всем кластерам."
    )
    days_without_sales_cluster: int = Field(
        ..., description="Количество дней без продаж в кластере."
    )
    excess_stock_count: int = Field(
        ..., description="Количество излишков с поставки, которые доступны к вывозу."
    )
    expiring_stock_count: int = Field(
        ..., description="Количество единиц товара с истекающим сроком годности."
    )
    idc: float = Field(
        ..., description="Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней по всем кластерам."
    )
    idc_cluster: float = Field(
        ..., description="Количество дней, на которое хватит остатка товара с учётом среднесуточных продаж за 28 дней в кластере."
    )
    item_tags: list[ItemTag] = Field(
        ..., description="Теги товара."
    )
    name: str = Field(
        ..., description="Название товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    other_stock_count: int = Field(
        ..., description="Количество единиц товара, проходящих проверку."
    )
    requested_stock_count: int = Field(
        ..., description="Количество единиц товара в заявках на поставку."
    )
    return_from_customer_stock_count: int = Field(
        ..., description="Количество единиц товара в процессе возврата от покупателей."
    )
    return_to_seller_stock_count: int = Field(
        ..., description="Количество единиц товара, готовящихся к вывозу по вашей заявке."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    stock_defect_stock_count: int = Field(
        ..., description="Количество брака, доступное к вывозу со стока."
    )
    transit_defect_stock_count: int = Field(
        ..., description="Количество брака, доступное к вывозу с поставки."
    )
    transit_stock_count: int = Field(
        ..., description="Количество единиц товара в поставках в пути."
    )
    turnover_grade: TurnoverGrade = Field(
        ..., description="Статус ликвидности товара по всем кластерам."
    )
    turnover_grade_cluster: TurnoverGrade = Field(
        ..., description="Статус ликвидности товара в кластере."
    )
    valid_stock_count: int = Field(
        ..., description="Количество товаров, которые готовятся к продаже. Соответствует столбцу «Готовим к продаже»."
    )
    waiting_docs_stock_count: int = Field(
        ..., description="Количество маркируемых товаров, которые ожидают ваших действий."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )
    warehouse_name: str = Field(
        ..., description="Название склада."
    )


class AnalyticsStocksResponse(BaseModel):
    """Схема ответа с аналитикой по остаткам.

    Attributes:
        items: Информация о товарах
    """
    items: list[AnalyticsStocksItem] = Field(
        ..., description="Информация о товарах."
    )