"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderStatusCounter"""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderStatusCounterItem(BaseModel):
    """Количество заявок на поставку в одном статусе.

    Attributes:
        count: Количество заявок в статусе
        order_state: Статус заявки на поставку (строкой; набор значений открыт)
    """
    count: Optional[int] = Field(
        None, description="Количество заявок в статусе."
    )
    order_state: Optional[str] = Field(
        None, description="Статус заявки на поставку."
    )


class SupplyOrderStatusCounterResponse(BaseModel):
    """Описывает схему ответа на запрос количества заявок на поставку по статусам.

    Attributes:
        items: Список количеств заявок, сгруппированных по статусу
    """
    items: Optional[list[SupplyOrderStatusCounterItem]] = Field(
        default_factory=list, description="Список количеств заявок, сгруппированных по статусу."
    )
