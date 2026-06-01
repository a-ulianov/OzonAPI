"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpWarehouseList"""
from pydantic import BaseModel, Field

from .entities import FbpWarehouse


class FbpWarehouseListResponse(BaseModel):
    """Схема ответа со списком партнёрских складов FBP.

    Attributes:
        warehouses: Список партнёрских складов
    """

    warehouses: list[FbpWarehouse] = Field(
        default_factory=list, description="Список партнёрских складов FBP."
    )
