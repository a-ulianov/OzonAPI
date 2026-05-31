"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerLabelGet"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ContainerError


class CarriageContainerLabelGetRequest(BaseModel):
    """Описывает схему запроса на получение этикетки по грузоместам.

    Attributes:
        container_ids: Идентификаторы грузомест
    """
    container_ids: list[str] = Field(
        ..., description="Идентификаторы грузомест."
    )


class CarriageContainerLabelGetContent(BaseModel):
    """Файл с этикеткой грузоместа.

    Attributes:
        content_type: Тип файла
        file_content: Содержание файла в бинарном виде (base64)
        file_name: Название файла
    """
    content_type: Optional[str] = Field(
        None, description="Тип файла."
    )
    file_content: Optional[str] = Field(
        None, description="Содержание файла в бинарном виде (base64)."
    )
    file_name: Optional[str] = Field(
        None, description="Название файла."
    )


class CarriageContainerLabelGetResponse(BaseModel):
    """Описывает схему ответа на запрос этикетки по грузоместам.

    Attributes:
        content: Файл с этикеткой
        error_containers: Ошибки грузомест, по которым не удалось сформировать этикетку
    """
    content: Optional[CarriageContainerLabelGetContent] = Field(
        None, description="Файл с этикеткой."
    )
    error_containers: Optional[list[ContainerError]] = Field(
        None, description="Ошибки грузомест, по которым не удалось сформировать этикетку."
    )
