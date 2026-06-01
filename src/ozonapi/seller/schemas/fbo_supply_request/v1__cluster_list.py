"""Схемы метода cluster_list (информация о кластерах и складах, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyClusterType


class ClusterListRequest(BaseModel):
    """Параметры запроса информации о кластерах.

    Attributes:
        cluster_ids: Идентификаторы кластеров
        cluster_type: Тип кластера
    """
    cluster_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы кластеров."
    )
    cluster_type: SupplyClusterType = Field(
        ..., description="Тип кластера."
    )


class ClusterWarehouse(BaseModel):
    """Склад логистического кластера.

    Attributes:
        name: Название склада
        type: Тип склада
        warehouse_id: Идентификатор склада
    """
    name: Optional[str] = Field(
        None, description="Название склада."
    )
    type: Optional[str] = Field(
        None, description="Тип склада."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )


class ClusterLogisticCluster(BaseModel):
    """Логистический кластер.

    Attributes:
        warehouses: Склады
    """
    warehouses: Optional[list[ClusterWarehouse]] = Field(
        None, description="Склады."
    )


class Cluster(BaseModel):
    """Кластер.

    Attributes:
        id: Идентификатор кластера
        logistic_clusters: Информация о складах кластера
        macrolocal_cluster_id: Идентификатор макролокального кластера
        name: Название кластера
        type: Тип кластера
    """
    id: Optional[int] = Field(
        None, description="Идентификатор кластера."
    )
    logistic_clusters: Optional[list[ClusterLogisticCluster]] = Field(
        None, description="Информация о складах кластера."
    )
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    name: Optional[str] = Field(
        None, description="Название кластера."
    )
    type: Optional[str] = Field(
        None, description="Тип кластера."
    )


class ClusterListResponse(BaseModel):
    """Ответ с информацией о кластерах и их складах.

    Attributes:
        clusters: Кластеры
    """
    clusters: Optional[list[Cluster]] = Field(
        None, description="Кластеры."
    )
