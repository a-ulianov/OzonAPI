"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerDocumentGet"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageContainerDocumentGetRequest(BaseModel):
    """Описывает схему запроса на получение документов по грузоместам.

    Attributes:
        container_ids: Идентификаторы грузомест
    """
    container_ids: list[str] = Field(
        ..., description="Идентификаторы грузомест."
    )


class CarriageContainerDocumentGetResponse(BaseModel):
    """Описывает схему ответа на запрос документов по грузоместам (ТрН и лист отгрузки).

    Notes:
        • Содержимое файла приходит в поле `file_content` в виде строки (base64).

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
