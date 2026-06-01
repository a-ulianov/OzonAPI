"""Схемы метода actions_discounts_task_list (список заявок на скидку, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.beta import DiscountTaskStatus


class ActionsDiscountsTaskListRequest(BaseModel):
    """Параметры запроса списка заявок на скидку.

    Attributes:
        last_id: Идентификатор последнего значения для пагинации
        limit: Количество значений в ответе (допустимо: 5, 10, 15, 20, 30, 50)
        status: Статус заявок
    """
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе (допустимо: 5, 10, 15, 20, 30, 50)."
    )
    status: Optional[DiscountTaskStatus] = Field(None, description="Статус заявок.")


class ActionsDiscountsTaskAutoModeratedInfo(BaseModel):
    """Информация об автомодерации заявки.

    Attributes:
        max_percent: Максимальный процент скидки
        max_price: Максимальная цена
        min_percent: Минимальный процент скидки
        min_price: Минимальная цена
    """
    max_percent: Optional[float] = Field(None, description="Максимальный процент скидки.")
    max_price: Optional[float] = Field(None, description="Максимальная цена.")
    min_percent: Optional[float] = Field(None, description="Минимальный процент скидки.")
    min_price: Optional[float] = Field(None, description="Минимальная цена.")


class ActionsDiscountsTask(BaseModel):
    """Заявка на скидку.

    Attributes:
        approved_discount: Одобренная скидка
        approved_price: Одобренная цена
        approved_quantity_max: Одобренное максимальное количество
        auto_moderated_info: Информация об автомодерации
        created_at: Дата создания заявки
        edited_till: Срок редактирования заявки
        edited_till_duration: Длительность срока редактирования
        email: Электронная почта покупателя
        end_at: Дата окончания действия скидки
        end_at_duration: Длительность действия скидки
        first_name: Имя покупателя
        id: Идентификатор заявки
        is_auto_moderated: Признак автомодерации
        last_name: Фамилия покупателя
        min_auto_price: Минимальная цена для автоодобрения
        moderated_at: Дата модерации
        name: Название товара
        original_price: Исходная цена
        patronymic: Отчество покупателя
        reduction_factor: Коэффициент снижения
        requested_discount: Запрошенная скидка
        requested_price: Запрошенная цена
        requested_quantity_max: Запрошенное максимальное количество
        sku: Идентификатор товара в системе Ozon — SKU
        status: Статус заявки
    """
    approved_discount: Optional[float] = Field(None, description="Одобренная скидка.")
    approved_price: Optional[float] = Field(None, description="Одобренная цена.")
    approved_quantity_max: Optional[int] = Field(
        None, description="Одобренное максимальное количество."
    )
    auto_moderated_info: Optional[ActionsDiscountsTaskAutoModeratedInfo] = Field(
        None, description="Информация об автомодерации."
    )
    created_at: Optional[str] = Field(None, description="Дата создания заявки.")
    edited_till: Optional[str] = Field(None, description="Срок редактирования заявки.")
    edited_till_duration: Optional[int] = Field(
        None, description="Длительность срока редактирования."
    )
    email: Optional[str] = Field(None, description="Электронная почта покупателя.")
    end_at: Optional[str] = Field(None, description="Дата окончания действия скидки.")
    end_at_duration: Optional[int] = Field(
        None, description="Длительность действия скидки."
    )
    first_name: Optional[str] = Field(None, description="Имя покупателя.")
    id: Optional[int] = Field(None, description="Идентификатор заявки.")
    is_auto_moderated: Optional[bool] = Field(None, description="Признак автомодерации.")
    last_name: Optional[str] = Field(None, description="Фамилия покупателя.")
    min_auto_price: Optional[float] = Field(
        None, description="Минимальная цена для автоодобрения."
    )
    moderated_at: Optional[str] = Field(None, description="Дата модерации.")
    name: Optional[str] = Field(None, description="Название товара.")
    original_price: Optional[float] = Field(None, description="Исходная цена.")
    patronymic: Optional[str] = Field(None, description="Отчество покупателя.")
    reduction_factor: Optional[float] = Field(None, description="Коэффициент снижения.")
    requested_discount: Optional[float] = Field(None, description="Запрошенная скидка.")
    requested_price: Optional[float] = Field(None, description="Запрошенная цена.")
    requested_quantity_max: Optional[int] = Field(
        None, description="Запрошенное максимальное количество."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    status: Optional[str] = Field(None, description="Статус заявки.")


class ActionsDiscountsTaskListResponse(BaseModel):
    """Ответ со списком заявок на скидку.

    Attributes:
        tasks: Список заявок
    """
    tasks: Optional[list[ActionsDiscountsTask]] = Field(
        None, description="Список заявок."
    )
