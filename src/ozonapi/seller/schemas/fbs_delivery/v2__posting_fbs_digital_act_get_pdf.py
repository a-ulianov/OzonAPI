"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetDigitalAct"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import BinaryFileResponse


class PostingFBSDigitalActGetPDFRequest(BaseModel):
    """Описывает схему запроса на получение листа отгрузки по перевозке.

    Attributes:
        id: Номер задания на формирование документов
        doc_type: Тип электронного документа
    """
    id: int = Field(
        ..., description="Номер задания на формирование документов (также идентификатор отгрузки)."
    )
    doc_type: Optional[str] = Field(
        None,
        description=(
            "Тип электронного документа: `act_of_acceptance` — лист отгрузки, "
            "`act_of_mismatch` — акт о расхождениях, `act_of_excess` — акт об излишках, "
            "`waybill` — транспортная накладная."
        )
    )


class PostingFBSDigitalActGetPDFResponse(BinaryFileResponse):
    """Описывает схему ответа на запрос листа отгрузки по перевозке.

    Attributes:
        content: Содержимое PDF-файла в виде байтов
    """
    pass
