"""Схемы метода cargoes_get (информация о грузоместах, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesGetSupplyRequest(BaseModel):
    """Поставка с грузоместами для запроса.

    Attributes:
        cargo_ids: Идентификаторы грузомест
        supply_id: Идентификатор поставки
    """
    cargo_ids: list[str] = Field(..., description="Идентификаторы грузомест.")
    supply_id: int = Field(..., description="Идентификатор поставки.")


class CargoesGetRequest(BaseModel):
    """Параметры запроса информации о грузоместах.

    Attributes:
        supplies: Поставки с грузоместами
    """
    supplies: list[CargoesGetSupplyRequest] = Field(
        ..., description="Поставки с грузоместами."
    )


class CargoesGetTimezone(BaseModel):
    """Часовой пояс времени прибытия.

    Attributes:
        iana_name: Наименование часового пояса в формате IANA
        offset: Смещение от UTC в секундах
    """
    iana_name: Optional[str] = Field(
        None, description="Наименование часового пояса в формате IANA."
    )
    offset: Optional[int] = Field(
        None, description="Смещение от UTC в секундах."
    )


class CargoesGetArrivalAt(BaseModel):
    """Время прибытия грузоместа.

    Attributes:
        date: Дата и время прибытия
        timezone_info: Часовой пояс
    """
    date: Optional[str] = Field(None, description="Дата и время прибытия.")
    timezone_info: Optional[CargoesGetTimezone] = Field(
        None, description="Часовой пояс."
    )


class CargoesGetTrackingInfo(BaseModel):
    """Информация об отслеживании грузоместа.

    Attributes:
        arrival_at: Время прибытия
        status: Статус грузоместа
        type: Тип события (`EXPECTED_ARRIVAL`, `ACTUAL_ARRIVAL`)
    """
    arrival_at: Optional[CargoesGetArrivalAt] = Field(
        None, description="Время прибытия."
    )
    status: Optional[str] = Field(None, description="Статус грузоместа.")
    type: Optional[str] = Field(
        None,
        description="Тип события. Возможные значения: `EXPECTED_ARRIVAL`, `ACTUAL_ARRIVAL`."
    )


class CargoesGetCargo(BaseModel):
    """Грузоместо поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargo_id: Идентификатор грузоместа
        content_type: Тип содержимого (`MONO`, `MIX`, `NONE`)
        placement_zone_type: Тип зоны размещения (`TYPE_SINGLE`, `MULTI`)
        tracking_info: Информация об отслеживании
        transport_cargo_id: Идентификатор транспортного грузоместа
        type: Тип грузоместа (`BOX`, `PALLET`)
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")
    content_type: Optional[str] = Field(
        None,
        description="Тип содержимого. Возможные значения: `MONO`, `MIX`, `NONE`."
    )
    placement_zone_type: Optional[str] = Field(
        None,
        description="Тип зоны размещения. Возможные значения: `TYPE_SINGLE`, `MULTI`."
    )
    tracking_info: Optional[CargoesGetTrackingInfo] = Field(
        None, description="Информация об отслеживании."
    )
    transport_cargo_id: Optional[int] = Field(
        None, description="Идентификатор транспортного грузоместа."
    )
    type: Optional[str] = Field(
        None, description="Тип грузоместа. Возможные значения: `BOX`, `PALLET`."
    )


class CargoesGetLimits(BaseModel):
    """Лимиты поставки по грузоместам.

    Attributes:
        max_box_count: Максимальное число коробок
        max_box_sku_count: Максимальное число SKU в коробке
        max_pallet_count: Максимальное число паллет
        max_transport_pallet_count: Максимальное число транспортных паллет
    """
    max_box_count: Optional[int] = Field(
        None, description="Максимальное число коробок."
    )
    max_box_sku_count: Optional[int] = Field(
        None, description="Максимальное число SKU в коробке."
    )
    max_pallet_count: Optional[int] = Field(
        None, description="Максимальное число паллет."
    )
    max_transport_pallet_count: Optional[int] = Field(
        None, description="Максимальное число транспортных паллет."
    )


class CargoesGetTransportArrivalAt(BaseModel):
    """Время прибытия транспортного грузоместа.

    Attributes:
        date: Дата и время прибытия
        timezone: Часовой пояс
    """
    date: Optional[str] = Field(None, description="Дата и время прибытия.")
    timezone: Optional[CargoesGetTimezone] = Field(
        None, description="Часовой пояс."
    )


class CargoesGetTransportTrackingInfo(BaseModel):
    """Информация об отслеживании транспортного грузоместа.

    Attributes:
        arrival_at: Время прибытия
        status: Статус транспортного грузоместа
        type: Тип события (`EXPECTED_ARRIVAL`, `ACTUAL_ARRIVAL`)
    """
    arrival_at: Optional[CargoesGetTransportArrivalAt] = Field(
        None, description="Время прибытия."
    )
    status: Optional[str] = Field(
        None, description="Статус транспортного грузоместа."
    )
    type: Optional[str] = Field(
        None,
        description="Тип события. Возможные значения: `EXPECTED_ARRIVAL`, `ACTUAL_ARRIVAL`."
    )


class CargoesGetTransportCargo(BaseModel):
    """Транспортное грузоместо поставки.

    Attributes:
        box_count: Число коробок в транспортном грузоместе
        summary_bundle_id: Идентификатор сводного товарного состава
        tracking_info: Информация об отслеживании
        transport_cargo_id: Идентификатор транспортного грузоместа
        type: Тип транспортного грузоместа (`PALLET`)
    """
    box_count: Optional[int] = Field(
        None, description="Число коробок в транспортном грузоместе."
    )
    summary_bundle_id: Optional[str] = Field(
        None, description="Идентификатор сводного товарного состава."
    )
    tracking_info: Optional[CargoesGetTransportTrackingInfo] = Field(
        None, description="Информация об отслеживании."
    )
    transport_cargo_id: Optional[int] = Field(
        None, description="Идентификатор транспортного грузоместа."
    )
    type: Optional[str] = Field(
        None, description="Тип транспортного грузоместа. Возможное значение: `PALLET`."
    )


class CargoesGetSupply(BaseModel):
    """Грузоместа поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargoes: Грузоместа поставки
        cargoes_bundle_id: Идентификатор товарного состава грузомест
        limits: Лимиты поставки
        supply_id: Идентификатор поставки
        transport_cargoes: Транспортные грузоместа поставки
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargoes: Optional[list[CargoesGetCargo]] = Field(
        None, description="Грузоместа поставки."
    )
    cargoes_bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава грузомест."
    )
    limits: Optional[CargoesGetLimits] = Field(
        None, description="Лимиты поставки."
    )
    supply_id: Optional[int] = Field(None, description="Идентификатор поставки.")
    transport_cargoes: Optional[list[CargoesGetTransportCargo]] = Field(
        None, description="Транспортные грузоместа поставки."
    )


class CargoesGetResponse(BaseModel):
    """Ответ с информацией о грузоместах.

    Attributes:
        supplies: Поставки с грузоместами
    """
    supplies: Optional[list[CargoesGetSupply]] = Field(
        None, description="Поставки с грузоместами."
    )
