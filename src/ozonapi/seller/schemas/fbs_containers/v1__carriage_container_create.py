"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageContainerCreateRequest(BaseModel):
    """Описывает схему запроса на создание грузоместа.

    Attributes:
        cargo_type: Тип грузоместа (`box` — коробка, `pallet` — палета)
        containers_count: Количество грузомест
        sort_type: Тип сортировки (`sort` — сортируемый, `non_sort` — несортируемый)
        warehouse_id: Идентификатор склада
    """
    cargo_type: str = Field(
        ..., description="Тип грузоместа: `box` — коробка, `pallet` — палета."
    )
    containers_count: int = Field(
        ..., description="Количество грузомест."
    )
    sort_type: str = Field(
        ..., description="Тип сортировки: `sort` — сортируемый, `non_sort` — несортируемый."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class CarriageContainerCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания грузоместа.

    Attributes:
        container_ids: Идентификаторы грузомест
    """
    container_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы грузомест."
    )
