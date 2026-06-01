"""https://docs.ozon.ru/api/seller/#operation/DiscountTask_List"""
from typing import Optional

from pydantic import BaseModel, Field


class DiscountTask(BaseModel):
    """Заявка покупателя на скидку.

    Attributes:
        id: Идентификатор заявки
        created_at: Дата создания заявки
        end_at: Дата окончания действия заявки
        edited_till: Дата, до которой можно изменить заявку
        customer_name: Имя покупателя
        sku: SKU товара
        user_comment: Комментарий покупателя
        seller_comment: Комментарий продавца
        requested_price: Запрошенная покупателем цена
        approved_price: Согласованная цена
        original_price: Изначальная цена товара
        discount: Размер скидки
        discount_percent: Процент скидки
        base_price: Базовая цена товара
        min_auto_price: Минимальная автоцена
        prev_task_id: Идентификатор предыдущей заявки
        is_damaged: Признак, что товар повреждён
        moderated_at: Дата модерации заявки
        approved_discount: Согласованный размер скидки
        approved_discount_percent: Согласованный процент скидки
        is_purchased: Признак, что товар был куплен
        is_auto_moderated: Признак автоматической модерации
        ozon_comment: Комментарий Ozon
        approved_quantity_min: Минимальное согласованное количество
        requested_quantity_min: Минимальное запрошенное количество
        requested_quantity_max: Максимальное запрошенное количество
        approved_quantity_max: Максимальное согласованное количество
        requested_price_with_fee: Запрошенная цена с учётом комиссии
        approved_price_with_fee: Согласованная цена с учётом комиссии
        approved_price_fee_percent: Процент комиссии согласованной цены
        requested_price_fee_percent: Процент комиссии запрошенной цены
        last_approved_price: Последняя согласованная цена
    """

    id: Optional[int] = Field(None, description="Идентификатор заявки.")
    created_at: Optional[str] = Field(None, description="Дата создания заявки.")
    end_at: Optional[str] = Field(None, description="Дата окончания действия заявки.")
    edited_till: Optional[str] = Field(None, description="Дата, до которой можно изменить заявку.")
    customer_name: Optional[str] = Field(None, description="Имя покупателя.")
    sku: Optional[int] = Field(None, description="SKU товара.")
    user_comment: Optional[str] = Field(None, description="Комментарий покупателя.")
    seller_comment: Optional[str] = Field(None, description="Комментарий продавца.")
    requested_price: Optional[float] = Field(None, description="Запрошенная покупателем цена.")
    approved_price: Optional[float] = Field(None, description="Согласованная цена.")
    original_price: Optional[float] = Field(None, description="Изначальная цена товара.")
    discount: Optional[float] = Field(None, description="Размер скидки.")
    discount_percent: Optional[float] = Field(None, description="Процент скидки.")
    base_price: Optional[float] = Field(None, description="Базовая цена товара.")
    min_auto_price: Optional[float] = Field(None, description="Минимальная автоцена.")
    prev_task_id: Optional[int] = Field(None, description="Идентификатор предыдущей заявки.")
    is_damaged: Optional[bool] = Field(None, description="Признак, что товар повреждён.")
    moderated_at: Optional[str] = Field(None, description="Дата модерации заявки.")
    approved_discount: Optional[float] = Field(None, description="Согласованный размер скидки.")
    approved_discount_percent: Optional[float] = Field(None, description="Согласованный процент скидки.")
    is_purchased: Optional[bool] = Field(None, description="Признак, что товар был куплен.")
    is_auto_moderated: Optional[bool] = Field(None, description="Признак автоматической модерации.")
    ozon_comment: Optional[str] = Field(None, description="Комментарий Ozon.")
    approved_quantity_min: Optional[int] = Field(None, description="Минимальное согласованное количество.")
    requested_quantity_min: Optional[int] = Field(None, description="Минимальное запрошенное количество.")
    requested_quantity_max: Optional[int] = Field(None, description="Максимальное запрошенное количество.")
    approved_quantity_max: Optional[int] = Field(None, description="Максимальное согласованное количество.")
    requested_price_with_fee: Optional[float] = Field(None, description="Запрошенная цена с учётом комиссии.")
    approved_price_with_fee: Optional[float] = Field(None, description="Согласованная цена с учётом комиссии.")
    approved_price_fee_percent: Optional[float] = Field(None, description="Процент комиссии согласованной цены.")
    requested_price_fee_percent: Optional[float] = Field(None, description="Процент комиссии запрошенной цены.")
    last_approved_price: Optional[float] = Field(None, description="Последняя согласованная цена.")


class ActionsDiscountsTaskListV1Request(BaseModel):
    """Схема запроса на получение списка заявок на скидку (API v1).

    Attributes:
        status: Статус заявок (NEW, SEEN, APPROVED, DECLINED, AUTODECLINED)
        page: Номер страницы
        limit: Количество заявок на странице
    """

    status: Optional[str] = Field(
        None, description="Статус заявок: NEW — новые, SEEN — просмотренные, "
                          "APPROVED — согласованные, DECLINED — отклонённые, "
                          "AUTODECLINED — отклонённые автоматически."
    )
    page: Optional[int] = Field(
        None, description="Номер страницы."
    )
    limit: Optional[int] = Field(
        None, description="Количество заявок на странице."
    )


class ActionsDiscountsTaskListV1Response(BaseModel):
    """Схема ответа со списком заявок на скидку (API v1).

    Attributes:
        result: Список заявок на скидку
    """

    result: Optional[list[DiscountTask]] = Field(
        None, description="Список заявок на скидку."
    )
