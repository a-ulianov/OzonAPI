"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActGetContainerLabels"""
from pydantic import BaseModel, Field

from .base import BinaryFileResponse


class PostingFBSActGetContainerLabelsRequest(BaseModel):
    """Описывает схему запроса на получение этикеток для грузового места.

    Attributes:
        id: Номер задания на формирование документов
    """
    id: int = Field(
        ..., description="Номер задания на формирование документов (также идентификатор отгрузки)."
    )


class PostingFBSActGetContainerLabelsResponse(BinaryFileResponse):
    """Описывает схему ответа на запрос этикеток для грузового места.

    Attributes:
        content: Содержимое PDF-файла с этикетками в виде байтов
    """
    pass
