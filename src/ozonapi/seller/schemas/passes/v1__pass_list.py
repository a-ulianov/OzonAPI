"""Схемы метода pass_list (список пропусков, v1)."""
from typing import Optional, Union

from pydantic import BaseModel, Field


class PassListFilter(BaseModel):
    """Фильтр выборки пропусков.

    Attributes:
        arrival_pass_ids: Фильтр по идентификаторам пропусков
        arrival_reason: Фильтр по цели въезда (`FBS_DELIVERY` — отгрузка, `FBS_RETURN` — вывоз возвратов)
        dropoff_point_ids: Фильтр по точкам отгрузки
        only_active_passes: `true`, чтобы получить только активные заявки на пропуск
        warehouse_ids: Фильтр по складам продавца
    """
    arrival_pass_ids: Optional[list[Union[int, str]]] = Field(
        None, description="Фильтр по идентификаторам пропусков."
    )
    arrival_reason: Optional[str] = Field(
        None,
        description="Фильтр по цели въезда: `FBS_DELIVERY` — отгрузка, "
                    "`FBS_RETURN` — вывоз возвратов."
    )
    dropoff_point_ids: Optional[list[str]] = Field(
        None, description="Фильтр по точкам отгрузки."
    )
    only_active_passes: Optional[bool] = Field(
        None, description="`true`, чтобы получить только активные заявки на пропуск."
    )
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Фильтр по складам продавца."
    )


class PassListRequest(BaseModel):
    """Параметры запроса списка пропусков.

    Attributes:
        cursor: Указатель для выборки следующих данных
        filter: Фильтр выборки
        limit: Ограничение по количеству записей в ответе (по умолчанию — 1000)
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[PassListFilter] = Field(None, description="Фильтр выборки.")
    limit: int = Field(
        ...,
        description="Ограничение по количеству записей в ответе. По умолчанию — 1000."
    )


class PassListArrivalPass(BaseModel):
    """Пропуск.

    Attributes:
        arrival_pass_id: Идентификатор пропуска
        arrival_reasons: Цель приезда
        arrival_time: Дата и время въезда в формате UTC
        driver_name: ФИО водителя
        driver_phone: Номер телефона водителя
        dropoff_point_id: Идентификатор точки отгрузки
        is_active: `true`, если заявка активна
        vehicle_license_plate: Номер автомобиля
        vehicle_model: Модель автомобиля
        warehouse_id: Идентификатор склада продавца
    """
    arrival_pass_id: Optional[int] = Field(None, description="Идентификатор пропуска.")
    arrival_reasons: Optional[list[str]] = Field(None, description="Цель приезда.")
    arrival_time: Optional[str] = Field(
        None, description="Дата и время въезда в формате UTC."
    )
    driver_name: Optional[str] = Field(None, description="ФИО водителя.")
    driver_phone: Optional[str] = Field(None, description="Номер телефона водителя.")
    dropoff_point_id: Optional[int] = Field(
        None, description="Идентификатор точки отгрузки."
    )
    is_active: Optional[bool] = Field(None, description="`true`, если заявка активна.")
    vehicle_license_plate: Optional[str] = Field(
        None, description="Номер автомобиля."
    )
    vehicle_model: Optional[str] = Field(None, description="Модель автомобиля.")
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )


class PassListResponse(BaseModel):
    """Ответ со списком пропусков.

    Attributes:
        arrival_passes: Список пропусков
        cursor: Указатель для выборки следующих данных
    """
    arrival_passes: list[PassListArrivalPass] = Field(
        default_factory=list, description="Список пропусков."
    )
    cursor: str = Field("", description="Указатель для выборки следующих данных.")
