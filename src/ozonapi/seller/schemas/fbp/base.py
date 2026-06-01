"""Общие базовые модели раздела FBP."""
from typing import Optional

from pydantic import BaseModel, Field


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
