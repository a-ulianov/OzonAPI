"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageCreateRequest(BaseModel):
    """Описывает схему запроса на создание отгрузки.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        departure_date: Дата отгрузки (по умолчанию — текущая дата)
        all_blr_traceable: Признак создания отгрузки с прослеживаемыми товарами
    """
    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки. По умолчанию — текущая дата."
    )
    all_blr_traceable: Optional[bool] = Field(
        None, description="`true`, если нужно создать отгрузку с прослеживаемыми товарами."
    )


class CarriageCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания отгрузки.

    Attributes:
        carriage_id: Идентификатор перевозки
    """
    carriage_id: Optional[int] = Field(
        None, description="Идентификатор перевозки."
    )
