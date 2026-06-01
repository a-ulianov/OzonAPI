"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderGet"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpCancellationState, FbpDeliveryDetails


class FbpOrderGetRequest(BaseModel):
    """Схема запроса информации о конкретной поставке.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpOrderGetResponse(BaseModel):
    """Схема ответа с информацией о конкретной поставке.

    Attributes:
        id: Идентификатор поставки
        supply_id: Идентификатор поставки (строковый)
        draft_id: Идентификатор черновика
        bundle_uuid: Идентификатор набора товаров
        order_number: Номер заявки на поставку
        warehouse_id: Идентификатор склада
        status: Статус поставки (`READY_TO_SUPPLY`, `FILLING_DELIVERY_DETAILS`,
            `COURIER_ASSIGNED`, `COURIER_PICKED_UP`, `ACCEPTANCE_AT_DROP_OFF_POINT`,
            `IN_TRANSIT_TO_STORAGE_WAREHOUSE`, `ACCEPTANCE_AT_STORAGE_WAREHOUSE`,
            `CANCELLED`)
        attention_reasons: Причины, требующие внимания (`OLD`, `TIME_SLOT_EXPIRED`)
        cancellation_state: Состояние отмены
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        created_date: Дата создания
        receive_date: Дата приёмки
        row_version: Версия записи
        can_be_cancelled: Признак возможности отмены
        has_label: Признак наличия этикетки
        has_consignment_note: Признак наличия транспортной накладной
        locked: Признак блокировки поставки
    """

    id: Optional[int] = Field(None, description="Идентификатор поставки.")
    supply_id: Optional[str] = Field(None, description="Идентификатор поставки (строковый).")
    draft_id: Optional[int] = Field(None, description="Идентификатор черновика.")
    bundle_uuid: Optional[str] = Field(None, description="Идентификатор набора товаров.")
    order_number: Optional[str] = Field(None, description="Номер заявки на поставку.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    status: Optional[str] = Field(
        None, description="Статус поставки (набор открытый — тип `str`)."
    )
    attention_reasons: list[str] = Field(
        default_factory=list,
        description="Причины, требующие внимания (набор открытый — тип `str`)."
    )
    cancellation_state: Optional[FbpCancellationState] = Field(
        None, description="Состояние отмены поставки."
    )
    delivery_details: Optional[FbpDeliveryDetails] = Field(
        None, description="Детали доставки поставки."
    )
    package_units_count: Optional[int] = Field(
        None, description="Количество грузовых единиц."
    )
    created_date: Optional[str] = Field(
        None, description="Дата создания в формате RFC3339."
    )
    receive_date: Optional[str] = Field(
        None, description="Дата приёмки в формате RFC3339."
    )
    row_version: Optional[int] = Field(None, description="Версия записи.")
    can_be_cancelled: Optional[bool] = Field(
        None, description="Признак возможности отмены."
    )
    has_label: Optional[bool] = Field(None, description="Признак наличия этикетки.")
    has_consignment_note: Optional[bool] = Field(
        None, description="Признак наличия транспортной накладной."
    )
    locked: Optional[bool] = Field(None, description="Признак блокировки поставки.")
