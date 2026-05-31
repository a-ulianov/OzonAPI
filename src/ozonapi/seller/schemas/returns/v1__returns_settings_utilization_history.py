"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationHistory"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsSettingsUtilizationHistoryItem(BaseModel):
    """Событие изменения настроек автоутилизации.

    Attributes:
        descriptions: Описание события
        updated_at: Дата обновления
        user_name: Имя пользователя
    """
    descriptions: Optional[list[str]] = Field(
        None, description="Описание события."
    )
    updated_at: Optional[str] = Field(
        None, description="Дата обновления."
    )
    user_name: Optional[str] = Field(
        None, description="Имя пользователя."
    )


class ReturnsSettingsUtilizationHistoryResponse(BaseModel):
    """Описывает схему ответа на запрос истории изменений автоутилизации.

    Attributes:
        history: История изменений
    """
    history: Optional[list[ReturnsSettingsUtilizationHistoryItem]] = Field(
        None, description="История изменений."
    )
