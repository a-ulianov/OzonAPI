"""https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsCandidates"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionsAutoAddProduct


class ActionsAutoAddProductsCandidatesRequest(BaseModel):
    """Схема запроса списка доступных для автодобавления в акцию товаров.

    Attributes:
        action_id: Идентификатор акции
        auto_add_date: Дата автодобавления товаров в акцию (обязательное поле)
        limit: Количество значений в ответе
        offset: Количество элементов, пропускаемых в ответе
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    auto_add_date: str = Field(
        ..., description="Дата автодобавления товаров в акцию в формате RFC3339. "
                         "Поле обязательно (живой API возвращает ошибку при его отсутствии, "
                         "хотя swagger помечает его необязательным)."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class ActionsAutoAddProductsCandidatesResponse(BaseModel):
    """Схема ответа со списком доступных для автодобавления в акцию товаров.

    Attributes:
        products: Список доступных для автодобавления товаров
        total: Общее количество товаров
    """

    products: list[ActionsAutoAddProduct] = Field(
        default_factory=list, description="Список доступных для автодобавления товаров."
    )
    total: Optional[int] = Field(
        None, description="Общее количество товаров."
    )
