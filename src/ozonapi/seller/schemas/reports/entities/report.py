"""Общая модель отчёта."""
from typing import Any, Optional

from pydantic import BaseModel, Field


class Report(BaseModel):
    """Информация о сгенерированном отчёте.

    Attributes:
        code: Уникальный идентификатор отчёта
        status: Статус генерации отчёта (`waiting`, `processing`, `success`, `failed`)
        report_type: Тип отчёта
        file: Ссылка на XLSX-файл
        params: Фильтры, указанные при создании отчёта
        created_at: Дата создания отчёта
        expires_at: Дата и время, до которых отчёт доступен
        error: Код ошибки при генерации отчёта
    """
    code: Optional[str] = Field(
        None, description="Уникальный идентификатор отчёта."
    )
    status: Optional[str] = Field(
        None, description="Статус генерации отчёта: `waiting`, `processing`, `success`, `failed`."
    )
    report_type: Optional[str] = Field(
        None, description="Тип отчёта."
    )
    file: Optional[str] = Field(
        None, description="Ссылка на XLSX-файл."
    )
    params: Optional[dict[str, Any]] = Field(
        None, description="Фильтры, указанные при создании отчёта."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания отчёта."
    )
    expires_at: Optional[str] = Field(
        None, description="Дата и время, до которых отчёт доступен."
    )
    error: Optional[str] = Field(
        None, description="Код ошибки при генерации отчёта."
    )
