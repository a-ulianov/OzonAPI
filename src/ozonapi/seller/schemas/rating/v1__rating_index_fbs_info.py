"""Схемы метода rating_index_fbs_info (индекс ошибок FBS и rFBS, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class RatingIndexFBSDynamics(BaseModel):
    """Значение индекса ошибок за день.

    Attributes:
        date: Дата в формате `YYYY-MM-DD`
        index_by_date: Значение индекса ошибок
        processing_costs_sum_by_date: Расходы на обработку ошибок
    """
    date: Optional[str] = Field(
        None, description="Дата в формате `YYYY-MM-DD`."
    )
    index_by_date: Optional[float] = Field(
        None, description="Значение индекса ошибок."
    )
    processing_costs_sum_by_date: Optional[float] = Field(
        None, description="Расходы на обработку ошибок."
    )


class RatingIndexFBSInfoResponse(BaseModel):
    """Ответ с индексом ошибок FBS и rFBS.

    Attributes:
        currency_code: Код валюты стоимости обработки ошибок
        defects: Индекс ошибок по дням
        index: Значение индекса ошибок за период
        period_from: Дата начала расчётного периода
        period_to: Дата окончания расчётного периода
        processing_costs_sum: Расходы на обработку ошибок за период
    """
    currency_code: Optional[str] = Field(
        None, description="Код валюты стоимости обработки ошибок."
    )
    defects: Optional[list[RatingIndexFBSDynamics]] = Field(
        None, description="Индекс ошибок по дням."
    )
    index: Optional[float] = Field(
        None, description="Значение индекса ошибок за период."
    )
    period_from: Optional[str] = Field(
        None, description="Дата начала расчётного периода."
    )
    period_to: Optional[str] = Field(
        None, description="Дата окончания расчётного периода."
    )
    processing_costs_sum: Optional[float] = Field(
        None, description="Расходы на обработку ошибок за период."
    )
