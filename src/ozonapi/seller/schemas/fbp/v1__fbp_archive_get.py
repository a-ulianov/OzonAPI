"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpArchiveGet"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    FbpArchiveDeclineReason,
    FbpArchiveSkuSummary,
    FbpDeliveryDetails,
)


class FbpArchiveGetRequest(BaseModel):
    """Схема запроса информации о завершённой поставке.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpArchiveGetResponse(BaseModel):
    """Схема ответа с информацией о завершённой поставке.

    Attributes:
        id: Идентификатор поставки
        supply_id: Идентификатор поставки (строковый)
        order_draft_id: Идентификатор черновика заявки
        order_number: Номер заявки на поставку
        bundle_id: Идентификатор набора товаров
        warehouse_id: Идентификатор склада
        business_flow_type_id: Идентификатор бизнес-процесса
        status: Статус (`COMPLETED`, `REJECTED_AT_SUPPLY_WAREHOUSE`,
            `CANCELLED_BY_SELLER`)
        bundle_sku_summary: Сводка по товарам
        decline_reason: Причина отклонения
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        act_file_uuid: Идентификатор файла акта
        has_act: Признак наличия акта
        has_label: Признак наличия этикетки
        created_date: Дата создания
        receive_date: Дата приёмки
        row_version: Версия записи
    """

    id: Optional[int] = Field(None, description="Идентификатор поставки.")
    supply_id: Optional[str] = Field(None, description="Идентификатор поставки (строковый).")
    order_draft_id: Optional[int] = Field(None, description="Идентификатор черновика заявки.")
    order_number: Optional[str] = Field(None, description="Номер заявки на поставку.")
    bundle_id: Optional[str] = Field(None, description="Идентификатор набора товаров.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    business_flow_type_id: Optional[int] = Field(
        None, description="Идентификатор бизнес-процесса."
    )
    status: Optional[str] = Field(
        None, description="Статус завершённой поставки (набор открытый — тип `str`)."
    )
    bundle_sku_summary: Optional[FbpArchiveSkuSummary] = Field(
        None, description="Сводка по товарам поставки."
    )
    decline_reason: Optional[FbpArchiveDeclineReason] = Field(
        None, description="Причина отклонения поставки."
    )
    delivery_details: Optional[FbpDeliveryDetails] = Field(
        None, description="Детали доставки поставки."
    )
    package_units_count: Optional[int] = Field(
        None, description="Количество грузовых единиц."
    )
    act_file_uuid: Optional[str] = Field(
        None, description="Идентификатор файла акта."
    )
    has_act: Optional[bool] = Field(None, description="Признак наличия акта.")
    has_label: Optional[bool] = Field(None, description="Признак наличия этикетки.")
    created_date: Optional[str] = Field(
        None, description="Дата создания в формате RFC3339."
    )
    receive_date: Optional[str] = Field(
        None, description="Дата приёмки в формате RFC3339."
    )
    row_version: Optional[int] = Field(None, description="Версия записи.")
