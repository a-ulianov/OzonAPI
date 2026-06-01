"""Схемы метода supply_order_content_update_validation (проверка состава, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderContentUpdateValidationRequest(BaseModel):
    """Параметры запроса проверки нового товарного состава.

    Attributes:
        new_bundle_id: Идентификатор нового товарного состава
        supply_id: Идентификатор поставки
    """
    new_bundle_id: str = Field(
        ..., description="Идентификатор нового товарного состава."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")


class SupplyOrderContentUpdateValidationApprovedItem(BaseModel):
    """Одобренный товар нового товарного состава.

    Attributes:
        barcode: Штрихкод товара
        item_link: Ссылка на карточку товара
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        origin_quantity: Исходное количество товара
        origin_total_volume_in_litres: Исходный суммарный объём в литрах
        quant: Размер кванта
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
        sku_quantity_limit: Лимит количества товара
        total_volume_in_litres: Суммарный объём в литрах
    """
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    item_link: Optional[str] = Field(
        None, description="Ссылка на карточку товара."
    )
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    origin_quantity: Optional[int] = Field(
        None, description="Исходное количество товара."
    )
    origin_total_volume_in_litres: Optional[float] = Field(
        None, description="Исходный суммарный объём в литрах."
    )
    quant: Optional[int] = Field(None, description="Размер кванта.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    sku_quantity_limit: Optional[int] = Field(
        None, description="Лимит количества товара."
    )
    total_volume_in_litres: Optional[float] = Field(
        None, description="Суммарный объём в литрах."
    )


class SupplyOrderContentUpdateValidationRestrictions(BaseModel):
    """Ограничения по отклонённому товару.

    Attributes:
        reasons_restrictions: Причины ограничений
        sku_has_no_sales_in_days: Дней без продаж товара
        sku_quantity_limit: Лимит количества товара
    """
    reasons_restrictions: Optional[list[str]] = Field(
        None, description="Причины ограничений."
    )
    sku_has_no_sales_in_days: Optional[int] = Field(
        None, description="Дней без продаж товара."
    )
    sku_quantity_limit: Optional[int] = Field(
        None, description="Лимит количества товара."
    )


class SupplyOrderContentUpdateValidationRejectedItem(BaseModel):
    """Отклонённый товар нового товарного состава.

    Attributes:
        barcode: Штрихкод товара
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        origin_quantity: Исходное количество товара
        origin_total_volume_in_litres: Исходный суммарный объём в литрах
        quantity: Количество товара
        rejection_reason: Причины отклонения
        restrictions: Ограничения по товару
        sku: Идентификатор товара в системе Ozon — SKU
        total_volume_in_litres: Суммарный объём в литрах
    """
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    origin_quantity: Optional[int] = Field(
        None, description="Исходное количество товара."
    )
    origin_total_volume_in_litres: Optional[float] = Field(
        None, description="Исходный суммарный объём в литрах."
    )
    quantity: Optional[int] = Field(None, description="Количество товара.")
    rejection_reason: Optional[list[str]] = Field(
        None, description="Причины отклонения."
    )
    restrictions: Optional[SupplyOrderContentUpdateValidationRestrictions] = Field(
        None, description="Ограничения по товару."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    total_volume_in_litres: Optional[float] = Field(
        None, description="Суммарный объём в литрах."
    )


class SupplyOrderContentUpdateValidationAssortment(BaseModel):
    """Проверенный товарный состав.

    Attributes:
        approved_items: Одобренные товары
        rejected_items: Отклонённые товары
        total_approved_item_count: Количество одобренных позиций
        total_approved_quantity: Суммарное одобренное количество
        total_approved_volume_in_litres: Суммарный одобренный объём в литрах
        total_rejected_item_count: Количество отклонённых позиций
        total_restricted_item_count: Количество ограниченных позиций
    """
    approved_items: Optional[
        list[SupplyOrderContentUpdateValidationApprovedItem]
    ] = Field(None, description="Одобренные товары.")
    rejected_items: Optional[
        list[SupplyOrderContentUpdateValidationRejectedItem]
    ] = Field(None, description="Отклонённые товары.")
    total_approved_item_count: Optional[int] = Field(
        None, description="Количество одобренных позиций."
    )
    total_approved_quantity: Optional[int] = Field(
        None, description="Суммарное одобренное количество."
    )
    total_approved_volume_in_litres: Optional[float] = Field(
        None, description="Суммарный одобренный объём в литрах."
    )
    total_rejected_item_count: Optional[int] = Field(
        None, description="Количество отклонённых позиций."
    )
    total_restricted_item_count: Optional[int] = Field(
        None, description="Количество ограниченных позиций."
    )


class SupplyOrderContentUpdateValidationResponse(BaseModel):
    """Ответ с результатом проверки нового товарного состава.

    Attributes:
        editing_errors: Ошибки редактирования
        validated_assortment: Проверенный товарный состав
    """
    editing_errors: Optional[list[str]] = Field(
        None, description="Ошибки редактирования."
    )
    validated_assortment: Optional[
        SupplyOrderContentUpdateValidationAssortment
    ] = Field(None, description="Проверенный товарный состав.")
