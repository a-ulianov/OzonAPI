"""Схемы метода warehouse_fbs_return_mile_check (проверка необходимости возвратной мили, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import FirstMileTypeV2


class WarehouseFBSReturnMileCheckRequest(BaseModel):
    """Параметры запроса проверки необходимости возвратной мили.

    Attributes:
        country_code: Код страны
        first_mile_type: Тип первой мили
        is_kgt: Признак приёма крупногабаритных товаров
        warehouse_id: Идентификатор склада
    """
    country_code: Optional[str] = Field(None, description="Код страны.")
    first_mile_type: Optional[FirstMileTypeV2] = Field(
        None, description="Тип первой мили."
    )
    is_kgt: Optional[bool] = Field(
        None, description="Признак приёма крупногабаритных товаров."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSReturnMileCheckResponse(BaseModel):
    """Ответ на проверку необходимости возвратной мили.

    Attributes:
        should_set_return_mile: Признак необходимости установки возвратной мили
        unavailability_reasons: Причины недоступности
    """
    should_set_return_mile: Optional[bool] = Field(
        None, description="Признак необходимости установки возвратной мили."
    )
    unavailability_reasons: Optional[list[str]] = Field(
        None, description="Причины недоступности."
    )
