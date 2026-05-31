"""https://docs.ozon.ru/api/seller/#operation/ActionsProducts"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionProduct


class ActionsProductsRequest(BaseModel):
    """Схема запроса на получение списка участвующих в акции товаров.

    Attributes:
        action_id: Идентификатор акции
        limit: Количество товаров на странице (максимум 1000)
        last_id: Идентификатор последнего значения на странице (для пагинации)
        offset: Количество элементов, которое будет пропущено в ответе
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    limit: int = Field(
        ..., description="Количество товаров на странице. Максимум — 1000."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице. "
                          "Передайте значение из ответа предыдущего запроса для пагинации."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class ActionsProductsResult(BaseModel):
    """Результат запроса участвующих в акции товаров.

    Attributes:
        products: Список товаров, участвующих в акции
        total: Общее количество товаров, участвующих в акции
    """

    products: Optional[list[ActionProduct]] = Field(
        None, description="Список товаров, участвующих в акции."
    )
    total: Optional[int] = Field(
        None, description="Общее количество товаров, участвующих в акции."
    )


class ActionsProductsResponse(BaseModel):
    """Схема ответа со списком участвующих в акции товаров.

    Attributes:
        result: Результат с товарами, участвующими в акции
    """

    result: Optional[ActionsProductsResult] = Field(
        None, description="Результат с товарами, участвующими в акции."
    )
