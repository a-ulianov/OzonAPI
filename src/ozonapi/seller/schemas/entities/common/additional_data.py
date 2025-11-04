from typing import Optional

from pydantic import BaseModel, Field


class AdditionalData(BaseModel):
    """Дополнительная информация.

    Attributes:
        key: Ключ
        value: Значение
    """
    key: Optional[str] = Field(
        None, description="Ключ."
    )
    value: Optional[str] = Field(
        None, description="Значение."
    )