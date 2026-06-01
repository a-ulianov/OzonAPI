"""https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsUpdate"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.localization import CurrencyCode
from .base import ActionsAutoAddPriceEntry, ActionsAutoAddRejected


class ActionsAutoAddProductsUpdateProduct(BaseModel):
    """Товар для добавления или обновления в автодобавлении в акцию.

    Attributes:
        product_id: Идентификатор товара
        action_price: Цена товара по акции
        quantity: Количество товара для автодобавления
        currency: Валюта цены
    """

    product_id: int = Field(
        ..., description="Идентификатор товара."
    )
    action_price: float = Field(
        ..., description="Цена товара по акции."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара для автодобавления."
    )
    currency: Optional[CurrencyCode] = Field(
        None, description="Валюта цены."
    )


class ActionsAutoAddProductsUpdateRequest(BaseModel):
    """Схема запроса на добавление или обновление товаров в автодобавлении в акцию.

    Attributes:
        action_id: Идентификатор акции
        auto_add_date: Дата автодобавления товаров в акцию (обязательное поле)
        to_update: Список товаров для добавления или обновления
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    auto_add_date: str = Field(
        ..., description="Дата автодобавления товаров в акцию в формате RFC3339. "
                         "Поле обязательно (живой API возвращает ошибку при его отсутствии, "
                         "хотя swagger помечает его необязательным)."
    )
    to_update: list[ActionsAutoAddProductsUpdateProduct] = Field(
        ..., description="Список товаров для добавления или обновления.",
        min_length=1
    )


class ActionsAutoAddProductsUpdateResponse(BaseModel):
    """Схема ответа на добавление или обновление товаров в автодобавлении в акцию.

    Attributes:
        updated_ids: Идентификаторы успешно обработанных товаров
        rejected: Товары, которые не удалось обработать
        below_min_price: Товары с ценой ниже минимально допустимой
        extremely_low_price: Товары с экстремально низкой ценой
        failed_price: Товары с некорректной ценой
    """

    updated_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы успешно обработанных товаров."
    )
    rejected: Optional[list[ActionsAutoAddRejected]] = Field(
        None, description="Товары, которые не удалось обработать, с причинами."
    )
    below_min_price: Optional[list[ActionsAutoAddPriceEntry]] = Field(
        None, description="Товары с ценой ниже минимально допустимой."
    )
    extremely_low_price: Optional[list[ActionsAutoAddPriceEntry]] = Field(
        None, description="Товары с экстремально низкой ценой."
    )
    failed_price: Optional[list[ActionsAutoAddPriceEntry]] = Field(
        None, description="Товары с некорректной ценой."
    )
