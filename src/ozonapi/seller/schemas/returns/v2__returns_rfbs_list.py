"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsListV2"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ReturnsRfbsProduct


class ReturnsRfbsCreatedAt(BaseModel):
    """Период создания заявки на возврат.

    Attributes:
        from_: Дата начала периода (сериализуется как `from`)
        to: Дата окончания периода
    """
    model_config = {'populate_by_name': True}

    from_: Optional[str] = Field(
        None, alias="from", description="Дата начала периода."
    )
    to: Optional[str] = Field(
        None, description="Дата окончания периода."
    )


class ReturnsRfbsListFilter(BaseModel):
    """Фильтр для получения списка заявок на возврат rFBS.

    Attributes:
        offer_id: Идентификатор товара в системе продавца
        posting_number: Номер отправления
        group_state: Фильтр по статусам заявок
        created_at: Период создания заявки
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    group_state: Optional[list[str]] = Field(
        None, description="Фильтр по статусам заявок."
    )
    created_at: Optional[ReturnsRfbsCreatedAt] = Field(
        None, description="Период создания заявки."
    )


class ReturnsRfbsListRequest(BaseModel):
    """Описывает схему запроса на получение списка заявок на возврат rFBS.

    Attributes:
        limit: Количество значений в ответе
        filter: Фильтр для поиска заявок
        last_id: Идентификатор последнего значения на странице
    """
    limit: int = Field(
        ..., description="Количество значений в ответе."
    )
    filter: Optional[ReturnsRfbsListFilter] = Field(
        None, description="Фильтр для поиска заявок."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения на странице."
    )


class ReturnsRfbsListState(BaseModel):
    """Статус заявки на возврат rFBS.

    Attributes:
        group_state: Статус заявки по применённому фильтру
        state: Статус заявки
        state_name: Название статуса заявки на русском
        money_return_state_name: Статус возврата денег
    """
    group_state: Optional[str] = Field(
        None, description="Статус заявки по применённому фильтру."
    )
    state: Optional[str] = Field(
        None, description="Статус заявки."
    )
    state_name: Optional[str] = Field(
        None, description="Название статуса заявки на русском."
    )
    money_return_state_name: Optional[str] = Field(
        None, description="Статус возврата денег."
    )


class ReturnsRfbsListItem(BaseModel):
    """Заявка на возврат rFBS в списке.

    Attributes:
        return_id: Идентификатор заявки на возврат
        return_number: Номер заявки на возврат
        client_name: Имя покупателя
        created_at: Дата создания заявки
        order_number: Номер заказа
        posting_number: Номер отправления
        product: Информация о товаре
        state: Статус заявки
    """
    return_id: Optional[int] = Field(
        None, description="Идентификатор заявки на возврат."
    )
    return_number: Optional[str] = Field(
        None, description="Номер заявки на возврат."
    )
    client_name: Optional[str] = Field(
        None, description="Имя покупателя."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания заявки."
    )
    order_number: Optional[str] = Field(
        None, description="Номер заказа."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    product: Optional[ReturnsRfbsProduct] = Field(
        None, description="Информация о товаре."
    )
    state: Optional[ReturnsRfbsListState] = Field(
        None, description="Статус заявки."
    )


class ReturnsRfbsListResponse(BaseModel):
    """Описывает схему ответа на запрос списка заявок на возврат rFBS.

    Attributes:
        returns: Список заявок на возврат
    """
    returns: Optional[list[ReturnsRfbsListItem]] = Field(
        None, description="Список заявок на возврат."
    )
