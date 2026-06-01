"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderDirectCancel"""
from pydantic import BaseModel, Field

from .base import FbpOrderValidationResult


class FbpOrderDirectCancelRequest(BaseModel):
    """Схема запроса отмены поставки (direct).

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpOrderDirectCancelResponse(FbpOrderValidationResult):
    """Схема ответа отмены поставки (direct).

    Notes:
        • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.
    """
