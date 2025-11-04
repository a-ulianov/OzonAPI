from typing import Optional

from pydantic import BaseModel, Field


class PostingFilterWith(BaseModel):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        analytics_data: Добавить в ответ данные аналитики (опционально)
        financial_data: Добавить в ответ финансовые данные (опционально)
        legal_info: Добавить в ответ юридическую информацию (опционально)
    """
    analytics_data: Optional[bool] = Field(
        False, description="Добавить в ответ данные аналитики."
    )
    financial_data: Optional[bool] = Field(
        False, description="Добавить в ответ финансовые данные."
    )
    legal_info: Optional[bool] = Field(
        False, description="Добавить в ответ юридическую информацию."
    )