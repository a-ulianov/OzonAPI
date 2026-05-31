"""Общая модель ошибки по грузоместу."""
from typing import Optional

from pydantic import BaseModel, Field


class ContainerError(BaseModel):
    """Ошибка обработки грузоместа.

    Attributes:
        container_id: Идентификатор грузоместа
        error_message: Текст ошибки
    """
    container_id: Optional[int] = Field(
        None, description="Идентификатор грузоместа."
    )
    error_message: Optional[str] = Field(
        None, description="Текст ошибки."
    )
