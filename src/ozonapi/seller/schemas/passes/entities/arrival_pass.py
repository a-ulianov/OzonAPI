"""Общие сущности раздела Пропуски."""
from pydantic import BaseModel, Field


class ArrivalPassDriverVehicle(BaseModel):
    """Общие данные о водителе и автомобиле для пропуска.

    Attributes:
        driver_name: ФИО водителя
        driver_phone: Номер телефона водителя
        vehicle_license_plate: Номер автомобиля
        vehicle_model: Модель автомобиля
    """
    driver_name: str = Field(..., description="ФИО водителя.")
    driver_phone: str = Field(..., description="Номер телефона водителя.")
    vehicle_license_plate: str = Field(..., description="Номер автомобиля.")
    vehicle_model: str = Field(..., description="Модель автомобиля.")
