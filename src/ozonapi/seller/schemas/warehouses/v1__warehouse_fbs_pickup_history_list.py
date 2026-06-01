"""Схемы метода warehouse_fbs_pickup_history_list (история отгрузок курьерам, v1)."""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseFBSPickUpHistoryListFilter(BaseModel):
    """Фильтр истории отгрузок курьерам.

    Attributes:
        planned_date: Запланированная дата отгрузки
        warehouse_id: Идентификаторы складов
        was_planned: Признак запланированной отгрузки
    """
    planned_date: Optional[str] = Field(
        None, description="Запланированная дата отгрузки."
    )
    warehouse_id: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )
    was_planned: Optional[bool] = Field(
        None, description="Признак запланированной отгрузки."
    )


class WarehouseFBSPickUpHistoryListRequest(BaseModel):
    """Параметры запроса истории отгрузок курьерам.

    Attributes:
        cursor: Указатель для выборки следующих данных
        filter: Фильтр истории отгрузок
        limit: Количество значений в ответе
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[WarehouseFBSPickUpHistoryListFilter] = Field(
        None, description="Фильтр истории отгрузок."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")


class WarehouseFBSPickUpHistoryEntity(BaseModel):
    """Запись истории отгрузки курьеру.

    Attributes:
        planned_date: Запланированная дата отгрузки
        status: Статус отгрузки
        updated_at: Дата и время обновления
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
        was_planned: Признак запланированной отгрузки
    """
    planned_date: Optional[str] = Field(
        None, description="Запланированная дата отгрузки."
    )
    status: Optional[str] = Field(None, description="Статус отгрузки.")
    updated_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время обновления."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")
    was_planned: Optional[bool] = Field(
        None, description="Признак запланированной отгрузки."
    )


class WarehouseFBSPickUpHistoryListResult(BaseModel):
    """Результат запроса истории отгрузок курьерам.

    Attributes:
        cursor: Указатель для выборки следующих данных
        history: Записи истории отгрузок
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    history: Optional[list[WarehouseFBSPickUpHistoryEntity]] = Field(
        None, description="Записи истории отгрузок."
    )


class WarehouseFBSPickUpHistoryListResponse(BaseModel):
    """Ответ с историей отгрузок курьерам.

    Attributes:
        result: Результат запроса истории отгрузок
    """
    result: Optional[WarehouseFBSPickUpHistoryListResult] = Field(
        None, description="Результат запроса истории отгрузок."
    )
