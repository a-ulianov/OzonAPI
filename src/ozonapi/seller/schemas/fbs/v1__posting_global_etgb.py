"""Схемы метода posting_global_etgb (таможенные декларации ETGB, v1)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostingGlobalEtgbDate(BaseModel):
    """Период формирования деклараций.

    Attributes:
        from_: Начало периода
        to_: Конец периода
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[str] = Field(None, alias="from", description="Начало периода.")
    to_: Optional[str] = Field(None, alias="to", description="Конец периода.")


class PostingGlobalEtgbRequest(BaseModel):
    """Параметры запроса таможенных деклараций ETGB.

    Attributes:
        date: Период формирования деклараций
    """
    date: Optional[PostingGlobalEtgbDate] = Field(
        None, description="Период формирования деклараций."
    )


class PostingGlobalEtgbDeclaration(BaseModel):
    """Таможенная декларация ETGB.

    Attributes:
        number: Номер декларации
        date: Дата декларации
        url: Ссылка на декларацию
    """
    number: Optional[str] = Field(None, description="Номер декларации.")
    date: Optional[str] = Field(None, description="Дата декларации.")
    url: Optional[str] = Field(None, description="Ссылка на декларацию.")


class PostingGlobalEtgbResult(BaseModel):
    """Декларация по отправлению.

    Attributes:
        posting_number: Номер отправления
        etgb: Таможенная декларация ETGB
    """
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    etgb: Optional[PostingGlobalEtgbDeclaration] = Field(
        None, description="Таможенная декларация ETGB."
    )


class PostingGlobalEtgbResponse(BaseModel):
    """Ответ с таможенными декларациями ETGB.

    Attributes:
        result: Декларации по отправлениям
    """
    result: Optional[list[PostingGlobalEtgbResult]] = Field(
        None, description="Декларации по отправлениям."
    )
