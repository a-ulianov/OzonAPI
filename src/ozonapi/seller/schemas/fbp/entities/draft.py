"""Общие сущности черновиков поставки FBP."""
from typing import Optional

from pydantic import BaseModel, Field

from .cancellation import FbpCancellationState
from .delivery import FbpDeliveryDetails


class FbpDeclineReason(BaseModel):
    """Причина отклонения черновика поставки FBP.

    Attributes:
        failed_sku_ids: SKU товаров, из-за которых отклонён черновик
        message: Текст причины отклонения
    """

    failed_sku_ids: list[str] = Field(
        default_factory=list,
        description="SKU товаров, из-за которых отклонён черновик."
    )
    message: Optional[str] = Field(
        None, description="Текст причины отклонения."
    )


class FbpDraftItem(BaseModel):
    """Элемент списка черновиков поставки FBP.

    Attributes:
        id: Идентификатор черновика
        supply_id: Идентификатор поставки
        bundle_id: Идентификатор набора товаров
        warehouse_id: Идентификатор склада
        status: Статус черновика (`DRAFT_STATUS_UNSPECIFIED`, `NEW`,
            `SUPPLY_VARIANT_CONFIRMATION`, `SUPPLY_NOT_CONFIRMED`)
        cancellation_state: Состояние отмены
        delivery_details: Детали доставки
        package_units_count: Количество грузовых единиц
        editable: Признак возможности редактирования
        is_cancelable: Признак возможности отмены
        is_deletable: Признак возможности удаления
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
    delivery_details: Optional[FbpDeliveryDetails] = Field(
        None, description="Детали доставки поставки."
    )
    package_units_count: Optional[int] = Field(
        None, description="Количество грузовых единиц."
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
    locked: Optional[bool] = Field(
        None, description="Признак блокировки черновика."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания в формате RFC3339."
    )
    deleted_at: Optional[str] = Field(
        None, description="Дата удаления в формате RFC3339."
    )
