"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderDirectSellerDlvEdit"""
from pydantic import BaseModel, Field

from .base import FbpOrderValidationResult


class FbpOrderDirectSellerDlvEditRequest(BaseModel):
    """Схема запроса обновления доставки силами продавца в поставке.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        driver_name: Имя водителя
        vehicle_number: Регистрационный номер транспортного средства
        vehicle_type: Тип транспортного средства
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    driver_name: str = Field(..., description="Имя водителя.")
    vehicle_number: str = Field(
        ..., description="Регистрационный номер транспортного средства."
    )
    vehicle_type: str = Field(..., description="Тип транспортного средства.")


class FbpOrderDirectSellerDlvEditResponse(FbpOrderValidationResult):
    """Схема ответа обновления доставки силами продавца в поставке.

    Notes:
        • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.
    """
