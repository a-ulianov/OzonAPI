"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutGetPDF"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutGetPDFResponse(BaseModel):
    """Описывает схему ответа на запрос штрихкода возвратной отгрузки в формате PDF.

    Notes:
        • Несмотря на заявленный в документации тип `application/pdf`, API возвращает JSON
          с полем `pdf` — содержимым PDF-файла в виде строки (base64).

    Attributes:
        pdf: Содержимое PDF-файла (base64)
    """
    pdf: Optional[str] = Field(
        None, description="Содержимое PDF-файла (base64)."
    )
