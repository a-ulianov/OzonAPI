"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderDropOffCancel"""
from pydantic import BaseModel, Field

from .base import FbpOrderValidationResult


class FbpOrderDropOffCancelRequest(BaseModel):
    """Схема запроса отмены drop-off поставки.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpOrderDropOffCancelResponse(FbpOrderValidationResult):
    """Схема ответа отмены drop-off поставки.

    Notes:
        • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.
    """
