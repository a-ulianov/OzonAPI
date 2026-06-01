"""Схемы метода warehouse_fbs_return_mile_info (информация о возвратной миле, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSReturnPoint


class WarehouseFBSReturnMileInfoRequest(BaseModel):
    """Параметры запроса информации о возвратной миле.

    Attributes:
        warehouse_ids: Идентификаторы складов
    """
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class WarehouseFBSReturnMileSetting(BaseModel):
    """Настройки возвратной мили склада.

    Attributes:
        is_return_mile_required: Признак обязательности возвратной мили
        return_point: Пункт возврата
        warehouse_id: Идентификатор склада
    """
    is_return_mile_required: Optional[bool] = Field(
        None, description="Признак обязательности возвратной мили."
    )
    return_point: Optional[WarehouseFBSReturnPoint] = Field(
        None, description="Пункт возврата."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class WarehouseFBSReturnMileInfoResponse(BaseModel):
    """Ответ с информацией о возвратной миле.

    Attributes:
        return_mile_settings: Настройки возвратной мили по складам
    """
    return_mile_settings: Optional[list[WarehouseFBSReturnMileSetting]] = Field(
        None, description="Настройки возвратной мили по складам."
    )
