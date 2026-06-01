"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftPickupCreate"""
from pydantic import BaseModel, Field

from .base import FbpDraftCreateResult


class FbpPickUpDeliveryDetails(BaseModel):
    """Детали pick-up поставки (точка забора) для создания/редактирования черновика.

    Attributes:
        address: Адрес забора
        comment: Комментарий
        date: Дата забора
        sender_name: Имя отправителя
        sender_phone: Телефон отправителя
    """

    address: str = Field(..., description="Адрес забора груза.")
    comment: str = Field(..., description="Комментарий к забору.")
    date: str = Field(..., description="Дата забора в формате RFC3339.")
    sender_name: str = Field(..., description="Имя отправителя.")
    sender_phone: str = Field(..., description="Телефон отправителя.")


class FbpDraftPickUpCreateRequest(BaseModel):
    """Схема запроса создания черновика pick-up поставки.

    Attributes:
        bundle_id: Идентификатор набора товаров
        delivery_details: Детали pick-up поставки
        package_units_count: Количество грузовых единиц
        warehouse_id: Идентификатор склада
    """

    bundle_id: str = Field(..., description="Идентификатор набора товаров.")
    delivery_details: FbpPickUpDeliveryDetails = Field(
        ..., description="Детали pick-up поставки."
    )
    package_units_count: int = Field(..., description="Количество грузовых единиц.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class FbpDraftPickUpCreateResponse(FbpDraftCreateResult):
    """Схема ответа создания черновика pick-up поставки.

    Notes:
        • Содержит идентификаторы созданного черновика и поставки, а также версию записи.
    """
