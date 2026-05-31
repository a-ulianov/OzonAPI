"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_DigitalActCheckStatus"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSDigitalActCheckStatusRequest(BaseModel):
    """Описывает схему запроса на проверку статуса формирования накладной.

    Attributes:
        id: Номер задания на формирование документов
    """
    id: int = Field(
        ..., description="Номер задания на формирование документов (также идентификатор отгрузки)."
    )


class PostingFBSDigitalActCheckStatusResponse(BaseModel):
    """Описывает схему ответа на запрос статуса формирования накладной.

    Notes:
        • Ответ возвращается без обёртки `result`.

    Attributes:
        id: Номер задания на формирование документов
        status: Статус формирования документов (`FORMING`, `FORMED`, `ERROR` и т.д.)
    """
    id: Optional[int] = Field(
        None, description="Номер задания на формирование документов."
    )
    status: Optional[str] = Field(
        None, description="Статус формирования документов: `FORMING` — ещё не готовы, `FORMED` — сформированы и т.д."
    )
