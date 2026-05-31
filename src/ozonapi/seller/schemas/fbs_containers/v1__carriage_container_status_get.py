"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerStatusGet"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageContainerStatusGetRequest(BaseModel):
    """Описывает схему запроса на получение статуса грузомест.

    Attributes:
        container_ids: Идентификаторы грузомест
    """
    container_ids: list[str] = Field(
        ..., description="Идентификаторы грузомест."
    )


class CarriageContainerStatus(BaseModel):
    """Статус грузоместа.

    Attributes:
        container_id: Идентификатор грузоместа
        status: Статус грузоместа
    """
    container_id: Optional[int] = Field(
        None, description="Идентификатор грузоместа."
    )
    status: Optional[str] = Field(
        None, description="Статус грузоместа."
    )


class CarriageContainerStatusGetResponse(BaseModel):
    """Описывает схему ответа на запрос статуса грузомест.

    Attributes:
        containers: Список грузомест со статусами
    """
    containers: Optional[list[CarriageContainerStatus]] = Field(
        None, description="Список грузомест."
    )
