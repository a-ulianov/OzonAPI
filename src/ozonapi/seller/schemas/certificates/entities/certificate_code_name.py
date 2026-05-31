"""Общая модель пары код-описание в разделе Сертификаты качества."""
from typing import Optional

from pydantic import BaseModel, Field


class CertificateCodeName(BaseModel):
    """Пара «код — описание».

    Attributes:
        code: Код значения
        name: Описание
    """
    code: Optional[str] = Field(
        None, description="Код значения."
    )
    name: Optional[str] = Field(
        None, description="Описание."
    )
