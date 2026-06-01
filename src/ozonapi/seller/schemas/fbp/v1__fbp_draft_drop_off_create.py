"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffCreate"""
from pydantic import BaseModel, Field

from .base import FbpDraftCreateResult


class FbpDraftDropOffCreateDeliveryDetails(BaseModel):
    """Детали доставки в drop-off пункт при создании черновика.

    Attributes:
        drop_off_date: Дата сдачи в drop-off пункт
        drop_off_point_id: Идентификатор drop-off пункта
        drop_off_province_uuid: Идентификатор провинции drop-off пункта
    """

    drop_off_date: str = Field(
        ..., description="Дата сдачи в drop-off пункт в формате RFC3339."
    )
    drop_off_point_id: int = Field(
        ..., description="Идентификатор drop-off пункта."
    )
    drop_off_province_uuid: str = Field(
        ..., description="Идентификатор провинции drop-off пункта."
    )


class FbpDraftDropOffCreateRequest(BaseModel):
    """Схема запроса создания черновика для доставки в drop-off пункт.

    Attributes:
        bundle_id: Идентификатор набора товаров
        delivery_details: Детали доставки в drop-off пункт
        package_units_count: Количество грузовых единиц
        warehouse_id: Идентификатор склада
    """

    bundle_id: str = Field(..., description="Идентификатор набора товаров.")
    delivery_details: FbpDraftDropOffCreateDeliveryDetails = Field(
        ..., description="Детали доставки в drop-off пункт."
    )
    package_units_count: int = Field(..., description="Количество грузовых единиц.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class FbpDraftDropOffCreateResponse(FbpDraftCreateResult):
    """Схема ответа создания черновика для доставки в drop-off пункт.

    Notes:
        • Содержит идентификаторы созданного черновика и поставки, а также версию записи.
    """
