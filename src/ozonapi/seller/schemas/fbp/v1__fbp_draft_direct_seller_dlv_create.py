"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectSellerDlvCreate"""
from pydantic import BaseModel, Field

from .base import FbpDraftCreateResult


class FbpDraftDirectSellerDlvCreateDeliveryDetails(BaseModel):
    """Детали доставки силами продавца при создании черновика.

    Attributes:
        driver_name: Имя водителя
        timeslot_start: Начало таймслота поставки
        vehicle_number: Регистрационный номер транспортного средства
        vehicle_type: Тип транспортного средства
    """

    driver_name: str = Field(
        ..., description="Имя водителя."
    )
    timeslot_start: str = Field(
        ..., description="Начало таймслота поставки в формате RFC3339."
    )
    vehicle_number: str = Field(
        ..., description="Регистрационный номер транспортного средства."
    )
    vehicle_type: str = Field(
        ..., description="Тип транспортного средства."
    )


class FbpDraftDirectSellerDlvCreateRequest(BaseModel):
    """Схема запроса создания черновика с доставкой силами продавца.

    Attributes:
        bundle_id: Идентификатор набора товаров
        delivery_details: Детали доставки силами продавца
        package_units_count: Количество грузовых единиц
        warehouse_id: Идентификатор склада
    """

    bundle_id: str = Field(
        ..., description="Идентификатор набора товаров."
    )
    delivery_details: FbpDraftDirectSellerDlvCreateDeliveryDetails = Field(
        ..., description="Детали доставки силами продавца."
    )
    package_units_count: int = Field(
        ..., description="Количество грузовых единиц."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class FbpDraftDirectSellerDlvCreateResponse(FbpDraftCreateResult):
    """Схема ответа создания черновика с доставкой силами продавца.

    Notes:
        • Содержит идентификаторы созданного черновика и поставки, а также версию записи.
    """
