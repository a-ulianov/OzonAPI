"""Схемы метода draft_create_info_v1 (информация о черновике, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DraftCreateInfoV1Request(BaseModel):
    """Параметры запроса информации о черновике заявки (версия 1).

    Attributes:
        operation_id: Идентификатор операции создания черновика
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции создания черновика."
    )


class DraftCreateInfoV1BundleId(BaseModel):
    """Товарный состав склада размещения.

    Attributes:
        bundle_id: Идентификатор комплекта товаров
        is_docless: Признак необходимости безбумажной поставки
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор комплекта товаров."
    )
    is_docless: Optional[bool] = Field(
        None, description="Признак необходимости безбумажной поставки."
    )


class DraftCreateInfoV1WarehouseStatus(BaseModel):
    """Статус склада размещения.

    Attributes:
        invalid_reason: Причина недоступности склада
        is_available: Признак доступности склада
        state: Статус скоринга склада
    """
    invalid_reason: Optional[str] = Field(
        None, description="Причина недоступности склада."
    )
    is_available: Optional[bool] = Field(
        None, description="Признак доступности склада."
    )
    state: Optional[str] = Field(
        None, description="Статус скоринга склада."
    )


class DraftCreateInfoV1SupplyWarehouse(BaseModel):
    """Склад размещения.

    Attributes:
        address: Адрес склада
        name: Название склада
        warehouse_id: Идентификатор склада
    """
    address: Optional[str] = Field(None, description="Адрес склада.")
    name: Optional[str] = Field(None, description="Название склада.")
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )


class DraftCreateInfoV1Warehouse(BaseModel):
    """Склад размещения в кластере.

    Attributes:
        bundle_ids: Товарный состав
        restricted_bundle_id: Комплект товаров с ограничениями
        status: Статус склада
        supply_warehouse: Склад размещения
        total_rank: Ранг склада в кластере
        total_score: Рейтинг склада
        travel_time_days: Предполагаемый срок доставки в днях
    """
    bundle_ids: Optional[list[DraftCreateInfoV1BundleId]] = Field(
        None, description="Товарный состав."
    )
    restricted_bundle_id: Optional[str] = Field(
        None, description="Комплект товаров с ограничениями."
    )
    status: Optional[DraftCreateInfoV1WarehouseStatus] = Field(
        None, description="Статус склада."
    )
    supply_warehouse: Optional[DraftCreateInfoV1SupplyWarehouse] = Field(
        None, description="Склад размещения."
    )
    total_rank: Optional[int] = Field(
        None, description="Ранг склада в кластере."
    )
    total_score: Optional[float] = Field(
        None, description="Рейтинг склада."
    )
    travel_time_days: Optional[int] = Field(
        None, description="Предполагаемый срок доставки в днях."
    )


class DraftCreateInfoV1Cluster(BaseModel):
    """Кластер размещения.

    Attributes:
        cluster_id: Идентификатор кластера
        cluster_name: Название кластера
        warehouses: Склады размещения
    """
    cluster_id: Optional[int] = Field(
        None, description="Идентификатор кластера."
    )
    cluster_name: Optional[str] = Field(
        None, description="Название кластера."
    )
    warehouses: Optional[list[DraftCreateInfoV1Warehouse]] = Field(
        None, description="Склады размещения."
    )


class DraftCreateInfoV1ItemValidation(BaseModel):
    """Ошибка валидации товара.

    Attributes:
        reasons: Причины ошибки
        sku: Идентификатор товара в системе Ozon — SKU
    """
    reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class DraftCreateInfoV1Error(BaseModel):
    """Ошибка расчёта черновика.

    Attributes:
        error_message: Сообщение об ошибке
        items_validation: Ошибки валидации товаров
        unknown_cluster_ids: Неизвестные идентификаторы кластеров
    """
    error_message: Optional[str] = Field(
        None, description="Сообщение об ошибке."
    )
    items_validation: Optional[list[DraftCreateInfoV1ItemValidation]] = Field(
        None, description="Ошибки валидации товаров."
    )
    unknown_cluster_ids: Optional[list[str]] = Field(
        None, description="Неизвестные идентификаторы кластеров."
    )


class DraftCreateInfoV1Response(BaseModel):
    """Ответ с информацией о черновике заявки (версия 1).

    Attributes:
        clusters: Кластеры размещения
        draft_id: Идентификатор черновика
        errors: Ошибки
        status: Статус расчёта черновика
    """
    clusters: Optional[list[DraftCreateInfoV1Cluster]] = Field(
        None, description="Кластеры размещения."
    )
    draft_id: Optional[int] = Field(
        None, description="Идентификатор черновика."
    )
    errors: Optional[list[DraftCreateInfoV1Error]] = Field(
        None, description="Ошибки."
    )
    status: Optional[str] = Field(
        None, description="Статус расчёта черновика."
    )
