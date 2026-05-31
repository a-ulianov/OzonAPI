"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerPlaceInto"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ContainerError


class CarriageContainerPlaceIntoRequest(BaseModel):
    """Описывает схему запроса на размещение коробок на палете.

    Attributes:
        parent_container_id: Идентификатор родительского грузоместа — палеты
        child_container_ids: Идентификаторы грузомест
    """
    parent_container_id: int = Field(
        ..., description="Идентификатор родительского грузоместа — палеты."
    )
    child_container_ids: list[str] = Field(
        ..., description="Идентификаторы грузомест."
    )


class CarriageContainerPlaceIntoResponse(BaseModel):
    """Описывает схему ответа на запрос размещения коробок на палете.

    Attributes:
        task_id: Идентификатор задания
        error_containers: Ошибки по грузоместам
    """
    task_id: Optional[int] = Field(
        None, description="Идентификатор задания."
    )
    error_containers: Optional[list[ContainerError]] = Field(
        None, description="Ошибки по грузоместам."
    )
