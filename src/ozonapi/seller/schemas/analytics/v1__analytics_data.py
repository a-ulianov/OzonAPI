"""https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsGetData"""
from typing import Optional

from pydantic import BaseModel, Field


class AnalyticsDataFilter(BaseModel):
    """Фильтр выборки данных аналитики.

    Attributes:
        key: Параметр сортировки/фильтрации (совпадает с метрикой или измерением)
        op: Операция сравнения
        value: Значение для сравнения
    """

    key: str = Field(
        ..., description="Параметр фильтрации (метрика или измерение)."
    )
    op: str = Field(
        ..., description="Операция сравнения: `EQ`, `GT`, `GTE`, `LT`, `LTE` и т. п."
    )
    value: str = Field(
        ..., description="Значение для сравнения."
    )


class AnalyticsDataSorting(BaseModel):
    """Параметр сортировки данных аналитики.

    Attributes:
        key: Метрика, по которой выполняется сортировка
        order: Направление сортировки
    """

    key: str = Field(
        ..., description="Метрика, по которой выполняется сортировка."
    )
    order: str = Field(
        ..., description="Направление сортировки: `ASC` или `DESC`."
    )


class AnalyticsDataRequest(BaseModel):
    """Схема запроса данных аналитики (Premium).

    Attributes:
        date_from: Дата начала периода (YYYY-MM-DD)
        date_to: Дата окончания периода (YYYY-MM-DD)
        dimension: Группировки данных (измерения)
        metrics: Запрашиваемые метрики
        filters: Фильтры выборки
        sort: Параметры сортировки
        limit: Количество значений в ответе
        offset: Количество элементов, пропускаемых в ответе
    """

    date_from: str = Field(
        ..., description="Дата начала периода в формате YYYY-MM-DD."
    )
    date_to: str = Field(
        ..., description="Дата окончания периода в формате YYYY-MM-DD."
    )
    dimension: list[str] = Field(
        ..., description="Группировки данных (измерения), например `sku`, `day`, `week`.",
        min_length=1
    )
    metrics: list[str] = Field(
        ..., description="Запрашиваемые метрики, например `revenue`, `ordered_units`.",
        min_length=1
    )
    filters: Optional[list[AnalyticsDataFilter]] = Field(
        None, description="Фильтры выборки."
    )
    sort: Optional[list[AnalyticsDataSorting]] = Field(
        None, description="Параметры сортировки."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class AnalyticsDataRowDimension(BaseModel):
    """Значение измерения в строке данных аналитики.

    Attributes:
        id: Идентификатор значения измерения
        name: Название значения измерения
    """

    id: Optional[str] = Field(
        None, description="Идентификатор значения измерения."
    )
    name: Optional[str] = Field(
        None, description="Название значения измерения."
    )


class AnalyticsDataRow(BaseModel):
    """Строка данных аналитики.

    Attributes:
        dimensions: Значения измерений строки
        metrics: Значения метрик строки
    """

    dimensions: list[AnalyticsDataRowDimension] = Field(
        default_factory=list, description="Значения измерений строки."
    )
    metrics: list[float] = Field(
        default_factory=list, description="Значения метрик строки."
    )


class AnalyticsDataResult(BaseModel):
    """Результат запроса данных аналитики.

    Attributes:
        data: Строки данных
        totals: Итоговые значения метрик
    """

    data: list[AnalyticsDataRow] = Field(
        default_factory=list, description="Строки данных."
    )
    totals: list[float] = Field(
        default_factory=list, description="Итоговые значения метрик."
    )


class AnalyticsDataResponse(BaseModel):
    """Схема ответа с данными аналитики.

    Attributes:
        result: Результат запроса
        timestamp: Время формирования ответа
    """

    result: Optional[AnalyticsDataResult] = Field(
        None, description="Результат запроса."
    )
    timestamp: Optional[str] = Field(
        None, description="Время формирования ответа."
    )
