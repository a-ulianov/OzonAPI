"""Общие базовые модели раздела FBP."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpOrderValidationError


class FbpOrderValidationResult(BaseModel):
    """Общий результат операции над действующей поставкой FBP.

    Attributes:
        is_error: Признак наличия ошибки
        error: Ошибка валидации поставки
        row_version: Версия записи
    """

    is_error: Optional[bool] = Field(
        None, description="Признак наличия ошибки."
    )
    error: Optional[FbpOrderValidationError] = Field(
        None, description="Ошибка валидации поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )


class FbpDraftCreateResult(BaseModel):
    """Результат создания черновика поставки FBP.

    Attributes:
        draft_id: Идентификатор созданного черновика
        supply_id: Идентификатор поставки
        row_version: Версия записи (для оптимистичной блокировки)
    """

    draft_id: Optional[int] = Field(
        None, description="Идентификатор созданного черновика."
    )
    supply_id: Optional[str] = Field(
        None, description="Идентификатор поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи (для оптимистичной блокировки)."
    )
