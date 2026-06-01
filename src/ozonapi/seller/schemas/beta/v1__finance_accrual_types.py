"""Схемы метода finance_accrual_types (справочник начислений, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceAccrualTypesRequest(BaseModel):
    """Параметры запроса справочника начислений.

    Notes:
        • Запрос без параметров.
    """


class FinanceAccrualType(BaseModel):
    """Тип начисления.

    Attributes:
        description: Описание типа начисления
        id: Идентификатор типа начисления
        name: Название типа начисления
    """
    description: Optional[str] = Field(None, description="Описание типа начисления.")
    id: Optional[int] = Field(None, description="Идентификатор типа начисления.")
    name: Optional[str] = Field(None, description="Название типа начисления.")


class FinanceAccrualTypesResponse(BaseModel):
    """Ответ со справочником начислений.

    Attributes:
        accrual_types: Типы начислений
    """
    accrual_types: Optional[list[FinanceAccrualType]] = Field(
        None, description="Типы начислений."
    )
