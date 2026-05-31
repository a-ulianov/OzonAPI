"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSGetAct"""
from pydantic import BaseModel, Field

from .base import BinaryFileResponse


class PostingFBSActGetPDFRequest(BaseModel):
    """Описывает схему запроса на получение PDF c документами.

    Attributes:
        id: Номер задания на формирование документов
    """
    id: int = Field(
        ..., description="Номер задания на формирование документов (также идентификатор отгрузки)."
    )


class PostingFBSActGetPDFResponse(BinaryFileResponse):
    """Описывает схему ответа на запрос PDF c документами.

    Attributes:
        content: Содержимое PDF-файла в виде байтов
    """
    pass
