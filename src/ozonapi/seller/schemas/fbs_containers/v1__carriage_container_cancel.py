"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerCancel"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ContainerError


class CarriageContainerCancelRequest(BaseModel):
    """Описывает схему запроса на отмену грузоместа.

    Attributes:
        container_ids: Идентификаторы грузомест
    """
    container_ids: list[str] = Field(
        ..., description="Идентификаторы грузомест."
    )


class CarriageContainerCancelResponse(BaseModel):
    """Описывает схему ответа на запрос отмены грузоместа.

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
