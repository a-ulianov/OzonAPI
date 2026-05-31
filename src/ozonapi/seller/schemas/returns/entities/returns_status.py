"""Общая модель статуса в разделе Возвраты."""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsStatus(BaseModel):
    """Статус возврата или компенсации.

    Attributes:
        id: Идентификатор статуса
        display_name: Название статуса
        sys_name: Системное название статуса
    """
    id: Optional[int] = Field(
        None, description="Идентификатор статуса."
    )
    display_name: Optional[str] = Field(
        None, description="Название статуса."
    )
    sys_name: Optional[str] = Field(
        None, description="Системное название статуса."
    )
