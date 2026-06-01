"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpBundleSummary, FbpCancellationState, FbpDeliveryDetails


class FbpOrderListRequest(BaseModel):
    """Схема запроса списка поставок.

    Attributes:
        count: Количество поставок в ответе
        last_id: Идентификатор последней поставки предыдущей страницы (пагинация)
    """

    count: int = Field(..., description="Количество поставок в ответе.")
    last_id: Optional[int] = Field(
        None,
        description="Идентификатор последней поставки предыдущей страницы "
                    "(для постраничной выборки)."
    )


class FbpOrderListItem(BaseModel):
    """Элемент списка поставок FBP.

    Attributes:
        id: Идентификатор поставки
        supply_id: Идентификатор поставки (строковый)
        order_number: Номер заявки на поставку
        warehouse_id: Идентификатор склада
        status: Статус поставки (набор открытый)
        attention_reasons: Причины, требующие внимания
        bundle_summary: Сводка по набору товаров
        cancellation_state: Состояние отмены
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        created_date: Дата создания
        receive_date: Дата приёмки
        can_be_cancelled: Признак возможности отмены
        has_label: Признак наличия этикетки
        has_consignment_note: Признак наличия транспортной накладной
        locked: Признак блокировки поставки
    """

    id: Optional[int] = Field(None, description="Идентификатор поставки.")
    supply_id: Optional[str] = Field(None, description="Идентификатор поставки (строковый).")
    order_number: Optional[str] = Field(None, description="Номер заявки на поставку.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    status: Optional[str] = Field(
        None, description="Статус поставки (набор открытый — тип `str`)."
    )
    attention_reasons: list[str] = Field(
        default_factory=list,
        description="Причины, требующие внимания (набор открытый — тип `str`)."
    )
    bundle_summary: Optional[FbpBundleSummary] = Field(
        None, description="Сводка по набору товаров."
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
    can_be_cancelled: Optional[bool] = Field(
        None, description="Признак возможности отмены."
    )
    has_label: Optional[bool] = Field(None, description="Признак наличия этикетки.")
    has_consignment_note: Optional[bool] = Field(
        None, description="Признак наличия транспортной накладной."
    )
    locked: Optional[bool] = Field(None, description="Признак блокировки поставки.")


class FbpOrderListResponse(BaseModel):
    """Схема ответа со списком поставок FBP.

    Attributes:
        items: Список поставок
        has_next: Признак наличия следующей страницы
        last_id: Идентификатор последней поставки в выборке
    """

    items: list[FbpOrderListItem] = Field(
        default_factory=list, description="Список поставок."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последней поставки в выборке."
    )
