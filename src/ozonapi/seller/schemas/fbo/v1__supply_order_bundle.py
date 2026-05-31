"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderBundle"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo import ItemSortField


class SupplyOrderBundleItemTagsCalculation(BaseModel):
    """Параметры расчёта тегов товаров для состава поставки.

    Attributes:
        dropoff_warehouse_id: Идентификатор склада отгрузки поставки
        storage_warehouse_ids: Список идентификаторов складов хранения
    """
    dropoff_warehouse_id: str = Field(
        ..., description="Идентификатор склада отгрузки поставки."
    )
    storage_warehouse_ids: list[str] = Field(
        ..., description="Список идентификаторов складов хранения."
    )


class SupplyOrderBundleRequest(BaseModel):
    """Описывает схему запроса на получение состава поставки или заявки на поставку.

    Attributes:
        bundle_ids: Список идентификаторов составов (бандлов)
        limit: Количество товаров на странице
        is_asc: `true`, чтобы сортировать по возрастанию
        item_tags_calculation: Параметры расчёта тегов товаров
        last_id: Идентификатор последнего значения SKU на странице
        sort_field: Поле сортировки
        query: Поисковый запрос (по названию, артикулу или SKU)
    """
    bundle_ids: list[str] = Field(
        ..., description="Список идентификаторов составов (бандлов)."
    )
    limit: int = Field(
        ..., description="Количество товаров на странице."
    )
    is_asc: Optional[bool] = Field(
        None, description="`true`, чтобы сортировать по возрастанию."
    )
    item_tags_calculation: Optional[SupplyOrderBundleItemTagsCalculation] = Field(
        None, description="Параметры расчёта тегов товаров."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения SKU на странице."
    )
    sort_field: Optional[ItemSortField] = Field(
        None, description="Поле сортировки."
    )
    query: Optional[str] = Field(
        None, description="Поисковый запрос (по названию, артикулу или SKU)."
    )


class SupplyOrderBundleItem(BaseModel):
    """Товар в составе поставки или заявки на поставку.

    Attributes:
        icon_path: Ссылка на изображение товара
        sku: Идентификатор товара в системе Ozon (SKU)
        name: Название товара
        offer_id: Идентификатор товара в системе продавца (артикул)
        quantity: Количество товара
        barcode: Штрихкод товара
        product_id: Идентификатор товара в системе Ozon (product_id)
        quant: Количество товаров в одной упаковке
        is_quant_editable: `true`, если количество товаров в упаковке можно изменить
        volume_in_litres: Объём товара в литрах
        total_volume_in_litres: Объём всех товаров в литрах
        contractor_item_code: Идентификатор товара в системе продавца (артикул)
        sfbo_attribute: Атрибут Super FBO (строкой)
        shipment_type: Тип упаковки (строкой)
        tags: Теги товара
        placement_zone: Зона размещения товара (строкой)
    """
    icon_path: Optional[str] = Field(
        None, description="Ссылка на изображение товара."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon (SKU)."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца (артикул)."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара."
    )
    barcode: Optional[str] = Field(
        None, description="Штрихкод товара."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon (product_id)."
    )
    quant: Optional[int] = Field(
        None, description="Количество товаров в одной упаковке."
    )
    is_quant_editable: Optional[bool] = Field(
        None, description="`true`, если количество товаров в упаковке можно изменить."
    )
    volume_in_litres: Optional[float] = Field(
        None, description="Объём товара в литрах."
    )
    total_volume_in_litres: Optional[float] = Field(
        None, description="Объём всех товаров в литрах."
    )
    contractor_item_code: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца (артикул)."
    )
    sfbo_attribute: Optional[str] = Field(
        None, description="Атрибут Super FBO."
    )
    shipment_type: Optional[str] = Field(
        None, description="Тип упаковки."
    )
    tags: Optional[list[str]] = Field(
        default_factory=list, description="Теги товара."
    )
    placement_zone: Optional[str] = Field(
        None, description="Зона размещения товара."
    )


class SupplyOrderBundleResponse(BaseModel):
    """Описывает схему ответа на запрос состава поставки или заявки на поставку.

    Attributes:
        items: Список товаров в составе
        total_count: Количество товаров в заявке
        has_next: Признак наличия следующей страницы
        last_id: Идентификатор последнего значения на странице
    """
    items: Optional[list[SupplyOrderBundleItem]] = Field(
        default_factory=list, description="Список товаров в составе."
    )
    total_count: Optional[int] = Field(
        None, description="Количество товаров в заявке."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )
