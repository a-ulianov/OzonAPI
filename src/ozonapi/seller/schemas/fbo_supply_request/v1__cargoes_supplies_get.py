"""Схемы метода cargoes_supplies_get (грузоместа в поставках, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesSuppliesGetRequest(BaseModel):
    """Параметры запроса информации о грузоместах в поставках.

    Attributes:
        supply_ids: Идентификаторы поставок
    """
    supply_ids: list[str] = Field(..., description="Идентификаторы поставок.")


class CargoesSuppliesGetCargo(BaseModel):
    """Грузоместо поставки.

    Attributes:
        barcode: Штрихкод грузоместа
        bundle_id: Идентификатор товарного состава
        cargo_id: Идентификатор грузоместа
    """
    barcode: Optional[str] = Field(None, description="Штрихкод грузоместа.")
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")


class CargoesSuppliesGetTransportCargo(BaseModel):
    """Транспортное грузоместо поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargoes: Вложенные грузоместа
        transport_cargo_id: Идентификатор транспортного грузоместа
        type: Тип транспортного грузоместа (`PALLET`)
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargoes: Optional[list[CargoesSuppliesGetCargo]] = Field(
        None, description="Вложенные грузоместа."
    )
    transport_cargo_id: Optional[int] = Field(
        None, description="Идентификатор транспортного грузоместа."
    )
    type: Optional[str] = Field(
        None, description="Тип транспортного грузоместа. Возможное значение: `PALLET`."
    )


class CargoesSuppliesGetSupply(BaseModel):
    """Грузоместа поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        cargoes_without_transport_cargoes: Грузоместа без транспортных грузомест
        supply_id: Идентификатор поставки
        transport_cargoes: Транспортные грузоместа поставки
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    cargoes_without_transport_cargoes: Optional[
        list[CargoesSuppliesGetCargo]
    ] = Field(None, description="Грузоместа без транспортных грузомест.")
    supply_id: Optional[int] = Field(None, description="Идентификатор поставки.")
    transport_cargoes: Optional[
        list[CargoesSuppliesGetTransportCargo]
    ] = Field(None, description="Транспортные грузоместа поставки.")


class CargoesSuppliesGetResponse(BaseModel):
    """Ответ с информацией о грузоместах в поставках.

    Attributes:
        not_found_supply_ids: Идентификаторы ненайденных поставок
        supplies_cargoes: Грузоместа по поставкам
    """
    not_found_supply_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы ненайденных поставок."
    )
    supplies_cargoes: Optional[list[CargoesSuppliesGetSupply]] = Field(
        None, description="Грузоместа по поставкам."
    )
