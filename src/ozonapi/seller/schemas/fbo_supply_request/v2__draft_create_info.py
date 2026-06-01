"""Схемы метода draft_create_info (информация о черновике, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class DraftCreateInfoRequest(BaseModel):
    """Параметры запроса информации о черновике заявки.

    Attributes:
        draft_id: Идентификатор черновика
    """
    draft_id: int = Field(..., description="Идентификатор черновика.")


class DraftCreateInfoAvailabilityStatus(BaseModel):
    """Статус доступности склада.

    Attributes:
        invalid_reason: Причина недоступности склада
        state: Статус доступности склада
    """
    invalid_reason: Optional[str] = Field(
        None, description="Причина недоступности склада."
    )
    state: Optional[str] = Field(
        None, description="Статус доступности склада."
    )


class DraftCreateInfoStorageWarehouse(BaseModel):
    """Склад хранения.

    Attributes:
        address: Адрес склада хранения
        name: Название склада хранения
        warehouse_id: Идентификатор склада хранения
    """
    address: Optional[str] = Field(
        None, description="Адрес склада хранения."
    )
    name: Optional[str] = Field(
        None, description="Название склада хранения."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада хранения."
    )


class DraftCreateInfoWarehouse(BaseModel):
    """Склад размещения.

    Attributes:
        availability_status: Статус доступности склада
        bundle_id: Идентификатор товарного состава
        restricted_bundle_id: Комплект товаров с ограничениями
        storage_warehouse: Склад хранения
        supply_tags: Метки товаров в заявке
        total_rank: Ранг склада в кластере
        total_score: Рейтинг склада
    """
    availability_status: Optional[DraftCreateInfoAvailabilityStatus] = Field(
        None, description="Статус доступности склада."
    )
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    restricted_bundle_id: Optional[str] = Field(
        None, description="Комплект товаров с ограничениями."
    )
    storage_warehouse: Optional[DraftCreateInfoStorageWarehouse] = Field(
        None, description="Склад хранения."
    )
    supply_tags: Optional[list[str]] = Field(
        None, description="Метки товаров в заявке."
    )
    total_rank: Optional[int] = Field(
        None, description="Ранг склада в кластере."
    )
    total_score: Optional[float] = Field(
        None, description="Рейтинг склада."
    )


class DraftCreateInfoCluster(BaseModel):
    """Кластер размещения.

    Attributes:
        cluster_name: Название кластера
        macrolocal_cluster_id: Идентификатор макролокального кластера
        supply_type: Тип поставки
        warehouses: Склады размещения
    """
    cluster_name: Optional[str] = Field(
        None, description="Название кластера."
    )
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    supply_type: Optional[str] = Field(
        None, description="Тип поставки."
    )
    warehouses: Optional[list[DraftCreateInfoWarehouse]] = Field(
        None, description="Склады размещения."
    )


class DraftCreateInfoRejectedItem(BaseModel):
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


class DraftCreateInfoItemValidation(BaseModel):
    """Ошибка валидации товаров кластера.

    Attributes:
        macrolocal_cluster_id: Идентификатор макролокального кластера
        rejected_items: Отклонённые товары
    """
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    rejected_items: Optional[list[DraftCreateInfoRejectedItem]] = Field(
        None, description="Отклонённые товары."
    )


class DraftCreateInfoError(BaseModel):
    """Ошибка расчёта черновика.

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
    items_validation: Optional[list[DraftCreateInfoItemValidation]] = Field(
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


class DraftCreateInfoResponse(BaseModel):
    """Ответ с информацией о черновике заявки.

    Attributes:
        clusters: Кластеры размещения
        errors: Ошибки
        status: Статус расчёта черновика
    """
    clusters: Optional[list[DraftCreateInfoCluster]] = Field(
        None, description="Кластеры размещения."
    )
    errors: Optional[list[DraftCreateInfoError]] = Field(
        None, description="Ошибки."
    )
    status: Optional[str] = Field(
        None, description="Статус расчёта черновика."
    )
