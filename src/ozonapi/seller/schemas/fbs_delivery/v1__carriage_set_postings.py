"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_SetPostings"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageSetPostingsResult(BaseModel):
    """Результат обработки отдельного отправления при изменении состава отгрузки.

    Attributes:
        posting_number: Номер отправления
        result: Результат обработки запроса (`true`, если запрос обработан)
        error: Описание ошибки
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    result: Optional[bool] = Field(
        None, description="Результат обработки запроса. `true`, если запрос был обработан."
    )
    error: Optional[str] = Field(
        None, description="Описание ошибки."
    )


class CarriageSetPostingsRequest(BaseModel):
    """Описывает схему запроса на изменение состава отгрузки.

    Attributes:
        carriage_id: Идентификатор отгрузки
        posting_numbers: Актуальный список отправлений
    """
    carriage_id: int = Field(
        ..., description="Идентификатор отгрузки."
    )
    posting_numbers: list[str] = Field(
        ..., description="Актуальный список отправлений."
    )


class CarriageSetPostingsResponse(BaseModel):
    """Описывает схему ответа на запрос изменения состава отгрузки.

    Attributes:
        result: Список результатов обработки отправлений
    """
    result: Optional[list[CarriageSetPostingsResult]] = Field(
        None, description="Список результатов обработки отправлений."
    )
