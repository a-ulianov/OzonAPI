"""Общие сущности раздела Доставка (/v1|/v2 delivery/*)."""
import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DeliveryLatLong(BaseModel):
    """Географические координаты точки.

    Attributes:
        lat: Широта
        long: Долгота
    """
    lat: Optional[float] = Field(None, description="Широта.")
    long: Optional[float] = Field(None, description="Долгота.")


class DeliveryViewport(BaseModel):
    """Прямоугольная область карты.

    Attributes:
        left_bottom: Координаты левого нижнего угла
        right_top: Координаты правого верхнего угла
    """
    left_bottom: Optional[DeliveryLatLong] = Field(
        None, description="Координаты левого нижнего угла."
    )
    right_top: Optional[DeliveryLatLong] = Field(
        None, description="Координаты правого верхнего угла."
    )


class DeliveryDateRange(BaseModel):
    """Диапазон дат и времени.

    Attributes:
        from_: Начало диапазона
        to_: Конец диапазона
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[datetime.datetime] = Field(
        None, alias="from", description="Начало диапазона."
    )
    to_: Optional[datetime.datetime] = Field(
        None, alias="to", description="Конец диапазона."
    )
