"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectTplDlvCreate"""
from pydantic import BaseModel, Field

from .base import FbpDraftCreateResult


class FbpDraftDirectTplDlvCreateDeliveryDetails(BaseModel):
    """Детали доставки сторонней транспортной компанией при создании черновика.

    Attributes:
        timeslot_start: Начало таймслота поставки
        tracking_number: Трек-номер отправления
        transport_company_name: Название транспортной компании
    """

    timeslot_start: str = Field(
        ..., description="Начало таймслота поставки в формате RFC3339."
    )
    tracking_number: str = Field(
        ..., description="Трек-номер отправления."
    )
    transport_company_name: str = Field(
        ..., description="Название транспортной компании."
    )


class FbpDraftDirectTplDlvCreateRequest(BaseModel):
    """Схема запроса создания черновика с доставкой сторонней транспортной компанией.

    Attributes:
        bundle_id: Идентификатор набора товаров
        delivery_details: Детали доставки сторонней транспортной компанией
        package_units_count: Количество грузовых единиц
        warehouse_id: Идентификатор склада
    """

    bundle_id: str = Field(
        ..., description="Идентификатор набора товаров."
    )
    delivery_details: FbpDraftDirectTplDlvCreateDeliveryDetails = Field(
        ..., description="Детали доставки сторонней транспортной компанией."
    )
    package_units_count: int = Field(
        ..., description="Количество грузовых единиц."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class FbpDraftDirectTplDlvCreateResponse(FbpDraftCreateResult):
    """Схема ответа создания черновика с доставкой сторонней транспортной компанией.

    Notes:
        • Содержит идентификаторы созданного черновика и поставки, а также версию записи.
    """
