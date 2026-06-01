"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftGet"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    FbpCancellationState,
    FbpDeclineReason,
    FbpDeliveryDetails,
)


class FbpDraftGetRequest(BaseModel):
    """Схема запроса информации о черновике поставки FBP.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(
        ..., description="Идентификатор поставки."
    )


class FbpDraftGetResponse(BaseModel):
    """Схема ответа с информацией о черновике поставки FBP.

    Attributes:
        id: Идентификатор черновика
        supply_id: Идентификатор поставки
        bundle_id: Идентификатор набора товаров
        warehouse_id: Идентификатор склада
        status: Статус черновика (`DRAFT_STATUS_UNSPECIFIED`, `NEW`,
            `SUPPLY_VARIANT_CONFIRMATION`, `SUPPLY_NOT_CONFIRMED`)
        cancellation_state: Состояние отмены
        decline_reason: Причина отклонения черновика
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        row_version: Версия записи
        editable: Признак возможности редактирования
        is_cancelable: Признак возможности отмены
        is_deletable: Признак возможности удаления
        is_registration_available: Признак доступности регистрации поставки
        locked: Признак блокировки черновика
        created_at: Дата создания
        deleted_at: Дата удаления
    """

    id: Optional[int] = Field(None, description="Идентификатор черновика.")
    supply_id: Optional[str] = Field(None, description="Идентификатор поставки.")
    bundle_id: Optional[str] = Field(None, description="Идентификатор набора товаров.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    status: Optional[str] = Field(
        None,
        description="Статус черновика. Известные значения: `DRAFT_STATUS_UNSPECIFIED`, "
                    "`NEW`, `SUPPLY_VARIANT_CONFIRMATION`, `SUPPLY_NOT_CONFIRMED` "
                    "(набор открытый — тип `str`)."
    )
    cancellation_state: Optional[FbpCancellationState] = Field(
        None, description="Состояние отмены поставки."
    )
    decline_reason: Optional[FbpDeclineReason] = Field(
        None, description="Причина отклонения черновика."
    )
    delivery_details: Optional[FbpDeliveryDetails] = Field(
        None, description="Детали доставки поставки."
    )
    package_units_count: Optional[int] = Field(
        None, description="Количество грузовых единиц."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи (для оптимистичной блокировки)."
    )
    editable: Optional[bool] = Field(
        None, description="Признак возможности редактирования."
    )
    is_cancelable: Optional[bool] = Field(
        None, description="Признак возможности отмены."
    )
    is_deletable: Optional[bool] = Field(
        None, description="Признак возможности удаления."
    )
    is_registration_available: Optional[bool] = Field(
        None, description="Признак доступности регистрации поставки."
    )
    locked: Optional[bool] = Field(
        None, description="Признак блокировки черновика."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания в формате RFC3339."
    )
    deleted_at: Optional[str] = Field(
        None, description="Дата удаления в формате RFC3339."
    )
