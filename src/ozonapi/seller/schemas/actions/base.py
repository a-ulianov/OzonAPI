"""Базовые (переиспользуемые) модели для методов раздела Акции."""
from typing import Optional

from pydantic import BaseModel, Field


class ActionProduct(BaseModel):
    """Товар, доступный для акции или участвующий в ней.

    Attributes:
        id: Идентификатор товара
        price: Текущая цена товара
        action_price: Цена товара по акции
        max_action_price: Максимально возможная цена товара по акции
        add_mode: Режим добавления товара в акцию
        min_stock: Минимальное количество товара для участия в акции
        stock: Количество товара на складе
        sku: SKU товара
    """

    id: Optional[int] = Field(
        None, description="Идентификатор товара."
    )
    price: Optional[float] = Field(
        None, description="Текущая цена товара."
    )
    action_price: Optional[float] = Field(
        None, description="Цена товара по акции."
    )
    max_action_price: Optional[float] = Field(
        None, description="Максимально возможная цена товара по акции."
    )
    add_mode: Optional[str] = Field(
        None, description="Режим добавления товара в акцию."
    )
    min_stock: Optional[int] = Field(
        None, description="Минимальное количество товара для участия в акции."
    )
    stock: Optional[int] = Field(
        None, description="Количество товара на складе."
    )
    sku: Optional[int] = Field(
        None, description="SKU товара."
    )


class ActionsProductsChangeRejected(BaseModel):
    """Товар, который не удалось добавить в акцию или убрать из неё.

    Attributes:
        product_id: Идентификатор товара
        reason: Причина отклонения
    """

    product_id: Optional[int] = Field(
        None, description="Идентификатор товара."
    )
    reason: Optional[str] = Field(
        None, description="Причина, по которой товар не был обработан."
    )


class ActionsProductsChangeResult(BaseModel):
    """Результат добавления товаров в акцию или удаления из неё.

    Attributes:
        product_ids: Идентификаторы успешно обработанных товаров
        rejected: Список товаров, которые не удалось обработать
    """

    product_ids: Optional[list[int]] = Field(
        None, description="Список идентификаторов успешно обработанных товаров."
    )
    rejected: Optional[list[ActionsProductsChangeRejected]] = Field(
        None, description="Список товаров, которые не удалось обработать, с причинами."
    )


class DiscountTaskFailDetail(BaseModel):
    """Детали ошибки при обработке заявки на скидку.

    Attributes:
        task_id: Идентификатор заявки
        error_for_user: Текст ошибки
    """

    task_id: Optional[int] = Field(
        None, description="Идентификатор заявки."
    )
    error_for_user: Optional[str] = Field(
        None, description="Текст ошибки, понятный пользователю."
    )


class DiscountTaskResult(BaseModel):
    """Результат согласования или отклонения заявок на скидку.

    Attributes:
        success_count: Количество успешно обработанных заявок
        fail_count: Количество заявок, обработанных с ошибкой
        fail_details: Детали ошибок по заявкам
    """

    success_count: Optional[int] = Field(
        None, description="Количество успешно обработанных заявок."
    )
    fail_count: Optional[int] = Field(
        None, description="Количество заявок, обработанных с ошибкой."
    )
    fail_details: Optional[list[DiscountTaskFailDetail]] = Field(
        None, description="Детали ошибок по заявкам."
    )


class DiscountTaskResponse(BaseModel):
    """Схема ответа на согласование или отклонение заявок на скидку.

    Notes:
        • Используется методами `actions_discounts_task_approve()` и
          `actions_discounts_task_decline()` — структура ответа у них одинаковая.

    Attributes:
        result: Результат обработки заявок
    """

    result: Optional[DiscountTaskResult] = Field(
        None, description="Результат обработки заявок на скидку."
    )
