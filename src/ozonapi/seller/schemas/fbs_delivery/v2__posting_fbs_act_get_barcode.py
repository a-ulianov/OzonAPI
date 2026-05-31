"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetBarcode"""
from pydantic import BaseModel, Field

from .base import BinaryFileResponse


class PostingFBSActGetBarcodeRequest(BaseModel):
    """Описывает схему запроса на получение штрихкода для отгрузки отправления.

    Attributes:
        id: Идентификатор перевозки
    """
    id: int = Field(
        ..., description="Идентификатор перевозки."
    )


class PostingFBSActGetBarcodeResponse(BinaryFileResponse):
    """Описывает схему ответа на запрос штрихкода для отгрузки отправления.

    Attributes:
        content: Содержимое PNG-изображения штрихкода в виде байтов
    """
    pass
