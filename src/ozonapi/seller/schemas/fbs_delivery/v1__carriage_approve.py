"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageApprove"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageApproveRequest(BaseModel):
    """Описывает схему запроса на подтверждение отгрузки.

    Attributes:
        carriage_id: Идентификатор отгрузки
        containers_count: Количество грузовых мест
    """
    carriage_id: int = Field(
        ..., description="Идентификатор отгрузки."
    )
    containers_count: Optional[int] = Field(
        None, description="Количество грузовых мест. Укажите, если вы подключены к схеме с грузовыми местами."
    )


class CarriageApproveResponse(BaseModel):
    """Описывает схему ответа на запрос подтверждения отгрузки.

    Notes:
        • При успешном подтверждении API возвращает пустой объект.
    """
    pass
