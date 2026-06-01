"""Схемы метода draft_direct_create (черновик заявки на прямую поставку, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyDeleteSkuMode
from .entities import DraftTypedClusterInfo


class DraftDirectCreateRequest(BaseModel):
    """Параметры запроса создания черновика заявки на прямую поставку.

    Attributes:
        cluster_info: Информация о кластере и товарном составе
        deletion_sku_mode: Режим удаления недоступных товаров
    """
    cluster_info: DraftTypedClusterInfo = Field(
        ..., description="Информация о кластере и товарном составе."
    )
    deletion_sku_mode: Optional[SupplyDeleteSkuMode] = Field(
        None, description="Режим удаления недоступных товаров."
    )
