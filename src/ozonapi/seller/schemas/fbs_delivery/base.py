"""Базовые модели раздела Доставка FBS."""
from typing import Optional

from pydantic import BaseModel, Field


class BinaryFileResponse(BaseModel):
    """Базовая схема ответа для эндпоинтов, возвращающих файл (PDF, PNG).

    Notes:
        • Тело ответа этих методов — не JSON, а файл; транспорт читает его как байты
          и помещает в поле `content`.

    Attributes:
        content: Содержимое файла в виде байтов
    """
    content: Optional[bytes] = Field(
        None, description="Содержимое файла в виде байтов."
    )
