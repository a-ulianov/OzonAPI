"""https://docs.ozon.ru/api/seller/#operation/Question_TopSku"""
from typing import Optional, Union

from pydantic import BaseModel, Field


class QuestionTopSkuRequest(BaseModel):
    """Описывает схему запроса на получение товаров с наибольшим количеством вопросов.

    Attributes:
        limit: Количество значений в ответе
    """
    limit: int = Field(
        ..., description="Количество значений в ответе."
    )


class QuestionTopSkuResponse(BaseModel):
    """Описывает схему ответа на запрос товаров с наибольшим количеством вопросов.

    Attributes:
        sku: Список идентификаторов товаров в системе Ozon — SKU
    """
    sku: Optional[list[Union[int, str]]] = Field(
        None, description="Список идентификаторов товаров в системе Ozon — SKU."
    )
