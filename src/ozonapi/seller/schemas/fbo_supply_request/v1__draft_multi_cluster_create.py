"""Схемы метода draft_multi_cluster_create (черновик заявки для нескольких кластеров, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyDeleteSkuMode
from .entities import DraftTypedClusterInfo, DraftTypedDeliveryInfo


class DraftMultiClusterCreateRequest(BaseModel):
    """Параметры запроса создания черновика заявки для нескольких кластеров.

    Attributes:
        clusters_info: Информация о кластерах и товарном составе
        deletion_sku_mode: Режим удаления недоступных товаров
        delivery_info: Информация о доставке до точки отгрузки
    """
    clusters_info: list[DraftTypedClusterInfo] = Field(
        ..., description="Информация о кластерах и товарном составе."
    )
    deletion_sku_mode: Optional[SupplyDeleteSkuMode] = Field(
        None, description="Режим удаления недоступных товаров."
    )
    delivery_info: DraftTypedDeliveryInfo = Field(
        ..., description="Информация о доставке до точки отгрузки."
    )
