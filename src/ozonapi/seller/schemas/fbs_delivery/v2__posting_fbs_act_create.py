"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSActCreateRequest(BaseModel):
    """Описывает схему запроса на подтверждение отгрузки и создание документов.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        departure_date: Дата отгрузки
        containers_count: Количество грузовых мест
    """
    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки."
    )
    containers_count: Optional[int] = Field(
        None, description="Количество грузовых мест. Укажите, если вы подключены к схеме с грузовыми местами."
    )


class PostingFBSActCreateAct(BaseModel):
    """Результат создания задания на формирование документов.

    Attributes:
        id: Номер задания на формирование штрихкода и документов
    """
    id: Optional[int] = Field(
        None, description="Номер задания на формирование штрихкода и документов."
    )


class PostingFBSActCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания документов.

    Attributes:
        result: Результат создания задания на формирование документов
    """
    result: Optional[PostingFBSActCreateAct] = Field(
        None, description="Результат создания задания на формирование документов."
    )
