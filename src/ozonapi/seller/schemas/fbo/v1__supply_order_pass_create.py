"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_CreateSupplyOrderPass"""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderVehicleInfo(BaseModel):
    """Данные о водителе и автомобиле.

    Attributes:
        driver_name: Имя водителя
        driver_phone: Телефон водителя
        vehicle_model: Модель автомобиля
        vehicle_number: Номер автомобиля
    """
    driver_name: str = Field(
        ..., description="Имя водителя."
    )
    driver_phone: str = Field(
        ..., description="Телефон водителя."
    )
    vehicle_model: str = Field(
        ..., description="Модель автомобиля."
    )
    vehicle_number: str = Field(
        ..., description="Номер автомобиля."
    )


class SupplyOrderPassCreateRequest(BaseModel):
    """Описывает схему запроса на указание данных о водителе и автомобиле.

    Attributes:
        supply_order_id: Идентификатор заявки на поставку
        vehicle: Данные о водителе и автомобиле
    """
    supply_order_id: int = Field(
        ..., description="Идентификатор заявки на поставку."
    )
    vehicle: SupplyOrderVehicleInfo = Field(
        ..., description="Данные о водителе и автомобиле."
    )


class SupplyOrderPassCreateResponse(BaseModel):
    """Описывает схему ответа на запрос указания данных о водителе и автомобиле.

    Attributes:
        operation_id: Идентификатор операции (для проверки статуса)
        error_reasons: Список причин ошибок (строками)
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции (для проверки статуса)."
    )
    error_reasons: Optional[list[str]] = Field(
        default_factory=list, description="Список причин ошибок."
    )
