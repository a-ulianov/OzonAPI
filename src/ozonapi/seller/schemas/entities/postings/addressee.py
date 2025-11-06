from typing import Optional

from pydantic import BaseModel, Field


class PostingAddressee(BaseModel):
    """Контактные данные покупателя/получателя."""
    name: Optional[str] = Field(
        None, description="Имя покупателя."
    )
    phone: Optional[str] = Field(
        None, description="Всегда возвращает пустую строку.."
    )
