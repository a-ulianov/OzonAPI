"""https://docs.ozon.ru/api/seller/#operation/SellerActionsList"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.seller_actions import (
    SellerActionStatus,
    SellerActionType,
)
from .base import SellerActionDiscountLevel


class SellerActionsListRequest(BaseModel):
    """Схема запроса списка акций продавца.

    Attributes:
        action_ids: Идентификаторы акций для фильтрации
        action_type: Механики акций для фильтрации
        status: Статусы акций для фильтрации
        search: Поиск по названию акции
        limit: Количество значений на странице
        offset: Количество элементов, пропускаемых в ответе
    """

    action_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы акций для фильтрации."
    )
    action_type: Optional[list[SellerActionType]] = Field(
        None, description="Механики акций для фильтрации."
    )
    status: Optional[list[SellerActionStatus]] = Field(
        None, description="Статусы акций для фильтрации."
    )
    search: Optional[str] = Field(
        None, description="Поиск по названию акции."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений на странице."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class SellerActionsListVoucherParameter(BaseModel):
    """Параметры промокода акции.

    Attributes:
        count_codes: Количество промокодов
        is_private: Является ли промокод приватным
        type: Тип промокода
    """

    count_codes: Optional[int] = Field(
        None, description="Количество промокодов."
    )
    is_private: Optional[bool] = Field(
        None, description="Является ли промокод приватным."
    )
    type: Optional[str] = Field(
        None, description="Тип промокода: `UNSPECIFIED`, `ONE`, `MULTIPLE` или `UNIQUE`."
    )


class SellerActionsListSegment(BaseModel):
    """Сегмент покупателей, которым доступна акция.

    Attributes:
        id: Идентификатор сегмента
        name: Название сегмента
        description: Описание сегмента
        type: Тип сегмента
    """

    id: Optional[int] = Field(
        None, description="Идентификатор сегмента."
    )
    name: Optional[str] = Field(
        None, description="Название сегмента."
    )
    description: Optional[str] = Field(
        None, description="Описание сегмента."
    )
    type: Optional[str] = Field(
        None, description="Тип сегмента: `UNSPECIFIED`, `OZON` или `SELLER`."
    )


class SellerActionsListPickedSegment(BaseModel):
    """Выбранные сегменты покупателей акции.

    Attributes:
        segments: Список сегментов
    """

    segments: list[SellerActionsListSegment] = Field(
        default_factory=list, description="Список сегментов."
    )


class SellerActionsListParameters(BaseModel):
    """Параметры акции продавца.

    Attributes:
        title: Название акции
        type: Механика акции
        status: Статус акции
        date_start: Дата и время начала акции
        date_end: Дата и время окончания акции
        discount_type: Тип скидки
        discount_value: Размер скидки
        min_action_percent: Минимальный процент скидки
        min_order_amount: Минимальная сумма заказа для применения скидки
        discount_levels: Уровни скидки для многоуровневой акции
        budget: Бюджет акции
        budget_spent: Израсходованный бюджет акции
        is_legal_entities_segment: Доступна ли акция сегменту юридических лиц
        auto_stop_action_reason: Причина автоматической остановки акции
        addresses: Адреса, к которым привязана акция
        warehouses: Склады, к которым привязана акция
        picked_segments: Выбранные сегменты покупателей
        voucher_parameters: Параметры промокода
    """

    title: Optional[str] = Field(
        None, description="Название акции."
    )
    type: Optional[str] = Field(
        None, description="Механика акции."
    )
    status: Optional[str] = Field(
        None, description="Статус акции."
    )
    date_start: Optional[str] = Field(
        None, description="Дата и время начала акции."
    )
    date_end: Optional[str] = Field(
        None, description="Дата и время окончания акции."
    )
    discount_type: Optional[str] = Field(
        None, description="Тип скидки."
    )
    discount_value: Optional[float] = Field(
        None, description="Размер скидки."
    )
    min_action_percent: Optional[float] = Field(
        None, description="Минимальный процент скидки."
    )
    min_order_amount: Optional[float] = Field(
        None, description="Минимальная сумма заказа для применения скидки."
    )
    discount_levels: Optional[list[SellerActionDiscountLevel]] = Field(
        None, description="Уровни скидки для многоуровневой акции."
    )
    budget: Optional[float] = Field(
        None, description="Бюджет акции."
    )
    budget_spent: Optional[float] = Field(
        None, description="Израсходованный бюджет акции."
    )
    is_legal_entities_segment: Optional[bool] = Field(
        None, description="Доступна ли акция сегменту юридических лиц."
    )
    auto_stop_action_reason: Optional[str] = Field(
        None, description="Причина автоматической остановки акции."
    )
    addresses: Optional[list[str]] = Field(
        None, description="Адреса, к которым привязана акция."
    )
    warehouses: Optional[list[str]] = Field(
        None, description="Склады, к которым привязана акция."
    )
    picked_segments: Optional[list[SellerActionsListPickedSegment]] = Field(
        None, description="Выбранные сегменты покупателей."
    )
    voucher_parameters: Optional[SellerActionsListVoucherParameter] = Field(
        None, description="Параметры промокода."
    )


class SellerActionsListAction(BaseModel):
    """Акция продавца.

    Attributes:
        action_id: Идентификатор акции
        action_parameters: Параметры акции
        sku_count: Количество товаров в акции
        is_participated: Участвует ли продавец в акции
        is_turn_on: Включена ли акция
        is_editable: Можно ли редактировать акцию
        allow_delete: Можно ли удалить акцию
        highlight_url: Ссылка на страницу акции
    """

    action_id: Optional[int] = Field(
        None, description="Идентификатор акции."
    )
    action_parameters: Optional[SellerActionsListParameters] = Field(
        None, description="Параметры акции."
    )
    sku_count: Optional[int] = Field(
        None, description="Количество товаров в акции."
    )
    is_participated: Optional[bool] = Field(
        None, description="Участвует ли продавец в акции."
    )
    is_turn_on: Optional[bool] = Field(
        None, description="Включена ли акция."
    )
    is_editable: Optional[bool] = Field(
        None, description="Можно ли редактировать акцию."
    )
    allow_delete: Optional[bool] = Field(
        None, description="Можно ли удалить акцию."
    )
    highlight_url: Optional[str] = Field(
        None, description="Ссылка на страницу акции."
    )


class SellerActionsListResponse(BaseModel):
    """Схема ответа со списком акций продавца.

    Attributes:
        actions: Список акций
        total: Общее количество акций
    """

    actions: list[SellerActionsListAction] = Field(
        default_factory=list, description="Список акций."
    )
    total: Optional[int] = Field(
        None, description="Общее количество акций."
    )
