"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectSellerDlvEdit"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpOrderDraftValidationError


class FbpDraftDirectSellerDlvEditRequest(BaseModel):
    """Схема запроса обновления информации о доставке силами продавца в черновике.

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


class FbpDraftDirectSellerDlvEditResponse(BaseModel):
    """Схема ответа обновления информации о доставке силами продавца.

    Attributes:
        is_error: Признак наличия ошибки
        error: Ошибка валидации черновика
        row_version: Версия записи
    """

    is_error: Optional[bool] = Field(
        None, description="Признак наличия ошибки."
    )
    error: Optional[FbpOrderDraftValidationError] = Field(
        None, description="Ошибка валидации черновика."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
