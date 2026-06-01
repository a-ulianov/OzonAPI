"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderPickUpCancel"""
from pydantic import BaseModel, Field

from .base import FbpOrderValidationResult


class FbpOrderPickUpCancelRequest(BaseModel):
    """Схема запроса отмены pick-up поставки.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpOrderPickUpCancelResponse(FbpOrderValidationResult):
    """Схема ответа отмены pick-up поставки.

    Notes:
        • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.
    """
