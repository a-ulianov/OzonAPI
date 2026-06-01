"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpArchiveList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    FbpArchiveDeclineReason,
    FbpArchiveSkuSummary,
    FbpDeliveryDetails,
)


class FbpArchiveListRequest(BaseModel):
    """Схема запроса списка завершённых поставок.

    Attributes:
        count: Количество поставок в ответе (строка с числом)
        last_id: Идентификатор последней поставки предыдущей страницы (строка с числом)
    """

    count: str = Field(
        ..., description="Количество поставок в ответе (строка с числом int32)."
    )
    last_id: Optional[str] = Field(
        None,
        description="Идентификатор последней поставки предыдущей страницы "
                    "(строка с числом int64, для постраничной выборки)."
    )


class FbpArchiveListItem(BaseModel):
    """Элемент списка завершённых поставок FBP.

    Attributes:
        supply_id: Идентификатор поставки (строковый)
        order_draft_id: Идентификатор черновика заявки
        bundle_id: Идентификатор набора товаров
        warehouse_id: Идентификатор склада
        external_order_id: Внешний идентификатор заявки
        whc_order_id: Идентификатор заявки на складе
        status: Статус (набор открытый)
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

    supply_id: Optional[str] = Field(None, description="Идентификатор поставки (строковый).")
    order_draft_id: Optional[int] = Field(None, description="Идентификатор черновика заявки.")
    bundle_id: Optional[str] = Field(None, description="Идентификатор набора товаров.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    external_order_id: Optional[str] = Field(None, description="Внешний идентификатор заявки.")
    whc_order_id: Optional[int] = Field(None, description="Идентификатор заявки на складе.")
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
    act_file_uuid: Optional[str] = Field(None, description="Идентификатор файла акта.")
    has_act: Optional[bool] = Field(None, description="Признак наличия акта.")
    has_label: Optional[bool] = Field(None, description="Признак наличия этикетки.")
    created_date: Optional[str] = Field(
        None, description="Дата создания в формате RFC3339."
    )
    receive_date: Optional[str] = Field(
        None, description="Дата приёмки в формате RFC3339."
    )
    row_version: Optional[int] = Field(None, description="Версия записи.")


class FbpArchiveListResponse(BaseModel):
    """Схема ответа со списком завершённых поставок FBP.

    Attributes:
        items: Список завершённых поставок
        has_next: Признак наличия следующей страницы
        last_id: Идентификатор последней поставки в выборке
    """

    items: list[FbpArchiveListItem] = Field(
        default_factory=list, description="Список завершённых поставок."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последней поставки в выборке."
    )
