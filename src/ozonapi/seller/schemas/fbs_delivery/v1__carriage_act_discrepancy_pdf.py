"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageActDiscrepancyPDF"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageActDiscrepancyPDFRequest(BaseModel):
    """Описывает схему запроса на получение акта о расхождениях по отгрузке FBS.

    Attributes:
        carriage_id: Идентификатор отгрузки
    """
    carriage_id: int = Field(
        ..., description="Идентификатор отгрузки."
    )


class CarriageActDiscrepancyPDFResponse(BaseModel):
    """Описывает схему ответа на запрос акта о расхождениях по отгрузке FBS.

    Notes:
        • Содержимое PDF-файла возвращается в поле `content` в виде строки
          (бинарные данные в base64-кодировке).

    Attributes:
        content: Содержание файла в бинарном виде (base64)
        name: Название файла
        type: Тип файла
    """
    content: Optional[str] = Field(
        None, description="Содержание файла в бинарном виде (base64)."
    )
    name: Optional[str] = Field(
        None, description="Название файла."
    )
    type: Optional[str] = Field(
        None, description="Тип файла."
    )
