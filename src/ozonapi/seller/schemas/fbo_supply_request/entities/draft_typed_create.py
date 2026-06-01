"""Общие модели типизированных черновиков заявок на поставку FBO."""
from typing import Optional

from pydantic import BaseModel, Field

from ....common.enumerations.fbo_supply_request import (
    SupplyDeliveryType,
    SupplyDropOffWarehouseType,
)


class DraftTypedItem(BaseModel):
    """Товар в товарном составе заявки.

    Attributes:
        quantity: Количество
        sku: Идентификатор товара в системе Ozon — SKU
    """
    quantity: int = Field(..., description="Количество.")
    sku: int = Field(..., description="Идентификатор товара в системе Ozon — SKU.")


class DraftTypedClusterInfo(BaseModel):
    """Информация о кластере и его товарном составе.

    Attributes:
        items: Товарный состав заявки
        macrolocal_cluster_id: Идентификатор макролокального кластера
    """
    items: list[DraftTypedItem] = Field(..., description="Товарный состав заявки.")
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )


class DraftTypedDropOffWarehouse(BaseModel):
    """Точка отгрузки заявки.

    Attributes:
        warehouse_id: Идентификатор склада
        warehouse_type: Тип точки отгрузки
    """
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
    warehouse_type: Optional[SupplyDropOffWarehouseType] = Field(
        None, description="Тип точки отгрузки."
    )


class DraftTypedDeliveryInfo(BaseModel):
    """Информация о доставке до точки отгрузки.

    Attributes:
        drop_off_warehouse: Точка отгрузки
        seller_warehouse_id: Идентификатор склада продавца
        type: Тип доставки
    """
    drop_off_warehouse: Optional[DraftTypedDropOffWarehouse] = Field(
        None, description="Точка отгрузки."
    )
    seller_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )
    type: Optional[SupplyDeliveryType] = Field(
        None, description="Тип доставки."
    )


class DraftTypedRejectedItem(BaseModel):
    """Отклонённый товар.

    Attributes:
        reasons: Причины отклонения
        sku: Идентификатор товара в системе Ozon — SKU
    """
    reasons: Optional[list[str]] = Field(
        None, description="Причины отклонения."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class DraftTypedItemsValidation(BaseModel):
    """Ошибки валидации товаров кластера.

    Attributes:
        macrolocal_cluster_id: Идентификатор макролокального кластера
        rejected_items: Отклонённые товары
    """
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    rejected_items: Optional[list[DraftTypedRejectedItem]] = Field(
        None, description="Отклонённые товары."
    )


class DraftTypedError(BaseModel):
    """Ошибка создания типизированного черновика.

    Attributes:
        error_message: Сообщение об ошибке
        error_reasons: Причины ошибки
        items_validation: Ошибки валидации товаров
        macrolocal_cluster_ids: Идентификаторы макролокальных кластеров
        message: Сообщение об ошибке
        skus: Список идентификаторов товаров
    """
    error_message: Optional[str] = Field(
        None, description="Сообщение об ошибке."
    )
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    items_validation: Optional[list[DraftTypedItemsValidation]] = Field(
        None, description="Ошибки валидации товаров."
    )
    macrolocal_cluster_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы макролокальных кластеров."
    )
    message: Optional[str] = Field(
        None, description="Сообщение об ошибке."
    )
    skus: Optional[list[str]] = Field(
        None, description="Список идентификаторов товаров."
    )


class DraftTypedCreateResponse(BaseModel):
    """Ответ на создание типизированного черновика заявки.

    Attributes:
        draft_id: Идентификатор черновика
        errors: Ошибки
    """
    draft_id: Optional[int] = Field(
        None, description="Идентификатор черновика."
    )
    errors: Optional[list[DraftTypedError]] = Field(
        None, description="Ошибки."
    )
