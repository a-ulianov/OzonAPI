"""Схемы метода cluster_list (макролокальные кластеры, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class ClusterListRequest(BaseModel):
    """Параметры запроса списка макролокальных кластеров.

    Notes:
        • Запрос без параметров.
    """


class ClusterListFulfillment(BaseModel):
    """Склад фулфилмента кластера.

    Attributes:
        name: Название склада
        warehouse_id: Идентификатор склада
    """
    name: Optional[str] = Field(None, description="Название склада.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class ClusterListCountry(BaseModel):
    """Страна кластера.

    Attributes:
        name: Название страны
        uid: Идентификатор страны
    """
    name: Optional[str] = Field(None, description="Название страны.")
    uid: Optional[str] = Field(None, description="Идентификатор страны.")


class ClusterListMacrolocalCluster(BaseModel):
    """Макролокальный кластер.

    Attributes:
        country: Страна кластера
        name: Название кластера
    """
    country: Optional[ClusterListCountry] = Field(None, description="Страна кластера.")
    name: Optional[str] = Field(None, description="Название кластера.")


class ClusterListData(BaseModel):
    """Данные кластера.

    Attributes:
        fulfillments: Склады фулфилмента
        macrolocal_cluster: Макролокальный кластер
    """
    fulfillments: Optional[list[ClusterListFulfillment]] = Field(
        None, description="Склады фулфилмента."
    )
    macrolocal_cluster: Optional[ClusterListMacrolocalCluster] = Field(
        None, description="Макролокальный кластер."
    )


class ClusterListItem(BaseModel):
    """Элемент списка кластеров.

    Attributes:
        data: Данные кластера
        macrolocal_cluster_id: Идентификатор макролокального кластера
    """
    data: Optional[ClusterListData] = Field(None, description="Данные кластера.")
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )


class ClusterListResponse(BaseModel):
    """Ответ со списком макролокальных кластеров.

    Attributes:
        result: Список кластеров
    """
    result: Optional[list[ClusterListItem]] = Field(
        None, description="Список кластеров."
    )
