"""Схемы метода warehouse_fbs_pickup_planning_list (склады для планирования отгрузок, v1)."""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseFBSPickUpPlanningWarehouse(BaseModel):
    """Склад для планирования отгрузки курьеру.

    Attributes:
        can_modify_pickup_plan: Признак возможности изменить план отгрузки
        has_postings_to_be_planned: Признак наличия отправлений для планирования
        is_pickup_planned: Признак запланированной отгрузки
        last_pickup_plan_date_at: Дата последнего планирования отгрузки
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    can_modify_pickup_plan: Optional[bool] = Field(
        None, description="Признак возможности изменить план отгрузки."
    )
    has_postings_to_be_planned: Optional[bool] = Field(
        None, description="Признак наличия отправлений для планирования."
    )
    is_pickup_planned: Optional[bool] = Field(
        None, description="Признак запланированной отгрузки."
    )
    last_pickup_plan_date_at: Optional[datetime.datetime] = Field(
        None, description="Дата последнего планирования отгрузки."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class WarehouseFBSPickUpPlanningListResult(BaseModel):
    """Результат запроса складов для планирования отгрузок.

    Attributes:
        warehouses: Список складов для планирования
    """
    warehouses: Optional[list[WarehouseFBSPickUpPlanningWarehouse]] = Field(
        None, description="Список складов для планирования."
    )


class WarehouseFBSPickUpPlanningListResponse(BaseModel):
    """Ответ со списком складов для планирования отгрузок.

    Attributes:
        result: Результат запроса складов для планирования
    """
    result: Optional[WarehouseFBSPickUpPlanningListResult] = Field(
        None, description="Результат запроса складов для планирования."
    )
