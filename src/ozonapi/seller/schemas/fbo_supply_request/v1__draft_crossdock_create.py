"""Схемы метода draft_crossdock_create (черновик заявки кросс-докингом, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyDeleteSkuMode
from .entities import DraftTypedClusterInfo, DraftTypedDeliveryInfo


class DraftCrossdockCreateRequest(BaseModel):
    """Параметры запроса создания черновика заявки кросс-докингом.

    Attributes:
        cluster_info: Информация о кластере и товарном составе
        deletion_sku_mode: Режим удаления недоступных товаров
        delivery_info: Информация о доставке до точки отгрузки
    """
    cluster_info: DraftTypedClusterInfo = Field(
        ..., description="Информация о кластере и товарном составе."
    )
    deletion_sku_mode: Optional[SupplyDeleteSkuMode] = Field(
        None, description="Режим удаления недоступных товаров."
    )
    delivery_info: DraftTypedDeliveryInfo = Field(
        ..., description="Информация о доставке до точки отгрузки."
    )
