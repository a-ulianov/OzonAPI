"""https://docs.ozon.ru/api/seller/#operation/ActionCandidates"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionProduct


class ActionsCandidatesRequest(BaseModel):
    """Схема запроса на получение списка доступных для акции товаров.

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


class ActionsCandidatesResult(BaseModel):
    """Результат запроса доступных для акции товаров.

    Attributes:
        products: Список товаров, доступных для акции
        total: Общее количество товаров, доступных для акции
    """

    products: Optional[list[ActionProduct]] = Field(
        None, description="Список товаров, доступных для акции."
    )
    total: Optional[int] = Field(
        None, description="Общее количество товаров, доступных для акции."
    )


class ActionsCandidatesResponse(BaseModel):
    """Схема ответа со списком доступных для акции товаров.

    Attributes:
        result: Результат с товарами, доступными для акции
    """

    result: Optional[ActionsCandidatesResult] = Field(
        None, description="Результат с товарами, доступными для акции."
    )
