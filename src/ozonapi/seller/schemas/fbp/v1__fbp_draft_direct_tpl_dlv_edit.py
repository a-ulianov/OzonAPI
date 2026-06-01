"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectTplDlvEdit"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpOrderDraftValidationError


class FbpDraftDirectTplDlvEditRequest(BaseModel):
    """Схема запроса редактирования черновика с доставкой сторонней ТК.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        tracking_number: Трек-номер отправления
        transport_company_name: Название транспортной компании
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    tracking_number: str = Field(..., description="Трек-номер отправления.")
    transport_company_name: str = Field(
        ..., description="Название транспортной компании."
    )


class FbpDraftDirectTplDlvEditResponse(BaseModel):
    """Схема ответа редактирования черновика с доставкой сторонней ТК.

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
