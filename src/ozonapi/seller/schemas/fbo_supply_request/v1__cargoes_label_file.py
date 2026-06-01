"""Схемы метода cargoes_label_file (PDF с этикетками грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelFileResponse(BaseModel):
    """Ответ с PDF-файлом этикеток грузомест.

    Notes:
        • Тело ответа этого метода — не JSON, а PDF-файл; транспорт читает его как
          байты и помещает в поле `content`.

    Attributes:
        content: Содержимое PDF-файла в виде байтов
    """
    content: Optional[bytes] = Field(
        None, description="Содержимое PDF-файла в виде байтов."
    )
