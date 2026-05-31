"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerRemoveFrom"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ContainerError


class CarriageContainerRemoveFromRequest(BaseModel):
    """Описывает схему запроса на удаление коробок с палеты.

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


class CarriageContainerRemoveFromResponse(BaseModel):
    """Описывает схему ответа на запрос удаления коробок с палеты.

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
