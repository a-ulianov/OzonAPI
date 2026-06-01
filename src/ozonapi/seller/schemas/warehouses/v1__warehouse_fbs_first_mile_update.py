"""Схемы метода warehouse_fbs_first_mile_update (обновление первой мили склада, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import FirstMileTypeV2


class WarehouseFBSFirstMileUpdateRequest(BaseModel):
    """Параметры запроса обновления первой мили склада FBS.

    Attributes:
        cut_in_time: Время на отгрузку в минутах
        drop_off_point_id: Идентификатор drop-off пункта
        first_mile_type: Тип первой мили
        timeslot_id: Идентификатор таймслота
        return_point_id: Идентификатор пункта возврата
        warehouse_id: Идентификатор склада
    """
    cut_in_time: Optional[int] = Field(
        None, description="Время на отгрузку в минутах."
    )
    drop_off_point_id: Optional[int] = Field(
        None, description="Идентификатор drop-off пункта."
    )
    first_mile_type: Optional[FirstMileTypeV2] = Field(
        None, description="Тип первой мили."
    )
    timeslot_id: Optional[int] = Field(None, description="Идентификатор таймслота.")
    return_point_id: Optional[int] = Field(
        None, description="Идентификатор пункта возврата."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSFirstMileUpdateResponse(BaseModel):
    """Ответ на обновление первой мили склада FBS.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(None, description="Идентификатор операции.")
