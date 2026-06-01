"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderPickUpDlvEdit"""
from pydantic import BaseModel, Field

from .base import FbpOrderValidationResult


class FbpOrderPickUpEditDetails(BaseModel):
    """Данные точки забора при редактировании pick-up поставки.

    Attributes:
        sender_name: Имя отправителя
        sender_phone: Телефон отправителя
    """

    sender_name: str = Field(..., description="Имя отправителя.")
    sender_phone: str = Field(..., description="Телефон отправителя.")


class FbpOrderPickUpDlvEditRequest(BaseModel):
    """Схема запроса изменения данных о точке забора в pick-up поставке.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        pickup_details: Данные точки забора
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    pickup_details: FbpOrderPickUpEditDetails = Field(
        ..., description="Данные точки забора."
    )


class FbpOrderPickUpDlvEditResponse(FbpOrderValidationResult):
    """Схема ответа изменения данных о точке забора в pick-up поставке.

    Notes:
        • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.
    """
