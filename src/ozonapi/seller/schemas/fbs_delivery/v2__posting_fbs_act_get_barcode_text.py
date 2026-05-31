"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetBarcodeText"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSActGetBarcodeTextRequest(BaseModel):
    """Описывает схему запроса на получение значения штрихкода для отгрузки.

    Attributes:
        id: Идентификатор перевозки
    """
    id: int = Field(
        ..., description="Идентификатор перевозки."
    )


class PostingFBSActGetBarcodeTextResponse(BaseModel):
    """Описывает схему ответа на запрос значения штрихкода для отгрузки.

    Attributes:
        result: Штрихкод в текстовом виде
    """
    result: Optional[str] = Field(
        None, description="Штрихкод в текстовом виде."
    )
