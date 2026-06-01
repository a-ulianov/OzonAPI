"""https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsList"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionsAutoAddProduct


class ActionsAutoAddProductsListRequest(BaseModel):
    """Схема запроса списка товаров из автодобавления в акцию.

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


class ActionsAutoAddProductsListResponse(BaseModel):
    """Схема ответа со списком товаров из автодобавления в акцию.

    Attributes:
        products: Список товаров из автодобавления
        total: Общее количество товаров
    """

    products: list[ActionsAutoAddProduct] = Field(
        default_factory=list, description="Список товаров из автодобавления."
    )
    total: Optional[int] = Field(
        None, description="Общее количество товаров."
    )
