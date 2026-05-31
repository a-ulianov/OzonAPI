"""Общая модель пары название-значение в разделе Сертификаты качества."""
from typing import Optional

from pydantic import BaseModel, Field


class CertificateNameValue(BaseModel):
    """Пара «название — значение справочника».

    Attributes:
        name: Название документа
        value: Значение справочника
    """
    name: Optional[str] = Field(
        None, description="Название документа."
    )
    value: Optional[str] = Field(
        None, description="Значение справочника."
    )
