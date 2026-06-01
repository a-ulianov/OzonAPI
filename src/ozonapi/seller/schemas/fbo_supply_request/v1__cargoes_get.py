"""Схемы метода cargoes_get (информация о грузоместах, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesGetRequest(BaseModel):
    """Параметры запроса информации о грузоместах.

    Attributes:
        supply_ids: Идентификаторы поставок
    """
    supply_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы поставок."
    )


class CargoesGetTrackingInfo(BaseModel):
    """Информация об отслеживании грузоместа.

    Attributes:
        date: Дата обновления статуса
        status: Статус грузоместа
        type: Тип события отслеживания
    """
    date: Optional[str] = Field(None, description="Дата обновления статуса.")
    status: Optional[str] = Field(None, description="Статус грузоместа.")
    type: Optional[str] = Field(None, description="Тип события отслеживания.")


class CargoesGetCargo(BaseModel):
    """Грузоместо поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargo_id: Идентификатор грузоместа
        content_type: Тип содержимого грузоместа
        placement_zone_type: Тип зоны размещения
        tracking_info: Информация об отслеживании
        type: Тип грузоместа
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")
    content_type: Optional[str] = Field(
        None, description="Тип содержимого грузоместа."
    )
    placement_zone_type: Optional[str] = Field(
        None, description="Тип зоны размещения."
    )
    tracking_info: Optional[CargoesGetTrackingInfo] = Field(
        None, description="Информация об отслеживании."
    )
    type: Optional[str] = Field(None, description="Тип грузоместа.")


class CargoesGetSupply(BaseModel):
    """Грузоместа поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargoes: Грузоместа поставки
        supply_id: Идентификатор поставки
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargoes: Optional[list[CargoesGetCargo]] = Field(
        None, description="Грузоместа поставки."
    )
    supply_id: Optional[int] = Field(None, description="Идентификатор поставки.")


class CargoesGetResponse(BaseModel):
    """Ответ с информацией о грузоместах.

    Attributes:
        supply: Поставки с грузоместами
    """
    supply: Optional[list[CargoesGetSupply]] = Field(
        None, description="Поставки с грузоместами."
    )
