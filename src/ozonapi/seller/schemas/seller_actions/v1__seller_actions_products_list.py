"""https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsList"""
from typing import Optional, Union

from pydantic import BaseModel, Field

from .base import SellerActionProduct


class SellerActionsProductsListRequest(BaseModel):
    """Схема запроса списка участвующих в акции товаров.

    Attributes:
        action_id: Идентификатор акции
        cursor: Указатель для выборки следующих данных
        limit: Количество значений в ответе
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    cursor: Optional[Union[int, str]] = Field(
        None, description="Указатель для выборки следующих данных (значение `cursor` "
                          "из предыдущего ответа)."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )


class SellerActionsProductsListResponse(BaseModel):
    """Схема ответа со списком участвующих в акции товаров.

    Attributes:
        cursor: Указатель для выборки следующих данных
        has_next: Признак наличия следующей страницы
        products: Список участвующих в акции товаров
    """

    cursor: Optional[Union[int, str]] = Field(
        None, description="Указатель для выборки следующих данных. Передайте его в "
                          "поле `cursor` следующего запроса. По данным живого API "
                          "`products/list` возвращает строку-токен (swagger объявляет "
                          "число); поле объявлено полиморфным для совместимости."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    products: list[SellerActionProduct] = Field(
        default_factory=list, description="Список участвующих в акции товаров."
    )
