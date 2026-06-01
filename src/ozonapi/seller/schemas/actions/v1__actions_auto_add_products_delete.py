"""https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsDelete"""
from typing import Optional

from pydantic import BaseModel, Field


class ActionsAutoAddProductsDeleteRequest(BaseModel):
    """Схема запроса на удаление товаров из автодобавления в акцию.

    Attributes:
        action_id: Идентификатор акции
        auto_add_date: Дата автодобавления товаров в акцию (обязательное поле)
        product_ids: Идентификаторы товаров для удаления
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    auto_add_date: str = Field(
        ..., description="Дата автодобавления товаров в акцию в формате RFC3339. "
                         "Поле обязательно (живой API возвращает ошибку при его отсутствии, "
                         "хотя swagger помечает его необязательным)."
    )
    product_ids: list[str] = Field(
        ..., description="Идентификаторы товаров для удаления из автодобавления.",
        min_length=1
    )


class ActionsAutoAddProductsDeleteResponse(BaseModel):
    """Схема ответа на удаление товаров из автодобавления в акцию.

    Attributes:
        product_ids: Идентификаторы удалённых товаров
    """

    product_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы удалённых из автодобавления товаров."
    )
