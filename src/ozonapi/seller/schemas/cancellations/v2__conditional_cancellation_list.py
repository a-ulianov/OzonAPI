"""Схемы метода conditional_cancellation_list (список заявок на отмену rFBS, v2)."""
import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ...common.enumerations.cancellations import (
    CancellationInitiator,
    CancellationStateFilter,
)


class ConditionalCancellationListFilters(BaseModel):
    """Фильтры списка заявок на отмену.

    Attributes:
        cancellation_initiator: Инициаторы отмены
        posting_number: Номера отправлений
        state: Статус заявки на отмену
    """
    cancellation_initiator: Optional[list[CancellationInitiator]] = Field(
        None, description="Инициаторы отмены."
    )
    posting_number: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )
    state: Optional[CancellationStateFilter] = Field(
        None, description="Статус заявки на отмену."
    )


class ConditionalCancellationListWith(BaseModel):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        counter: Добавить счётчики заявок по статусам
    """
    counter: Optional[bool] = Field(
        None, description="Добавить счётчики заявок по статусам."
    )


class ConditionalCancellationListRequest(BaseModel):
    """Параметры запроса списка заявок на отмену rFBS.

    Attributes:
        filters: Фильтры списка заявок
        last_id: Идентификатор последнего значения для пагинации
        limit: Количество значений в ответе
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    filters: Optional[ConditionalCancellationListFilters] = Field(
        None, description="Фильтры списка заявок."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    with_: Optional[ConditionalCancellationListWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class ConditionalCancellationReason(BaseModel):
    """Причина отмены.

    Attributes:
        id: Идентификатор причины отмены
        name: Название причины отмены
    """
    id: Optional[int] = Field(None, description="Идентификатор причины отмены.")
    name: Optional[str] = Field(None, description="Название причины отмены.")


class ConditionalCancellationState(BaseModel):
    """Статус заявки на отмену.

    Attributes:
        id: Идентификатор статуса
        name: Название статуса
        state: Системное значение статуса
    """
    id: Optional[int] = Field(None, description="Идентификатор статуса.")
    name: Optional[str] = Field(None, description="Название статуса.")
    state: Optional[str] = Field(None, description="Системное значение статуса.")


class ConditionalCancellationItem(BaseModel):
    """Заявка на отмену rFBS.

    Attributes:
        approve_comment: Комментарий при подтверждении заявки
        approve_date: Дата подтверждения заявки
        auto_approve_date: Дата автоматического подтверждения заявки
        cancellation_id: Идентификатор заявки на отмену
        cancellation_initiator: Инициатор отмены
        cancellation_reason: Причина отмены
        cancellation_reason_message: Комментарий к причине отмены
        cancelled_at: Дата создания заявки на отмену
        order_date: Дата оформления заказа
        posting_number: Номер отправления
        source_id: Идентификатор источника отмены
        state: Статус заявки на отмену
        tpl_integration_type: Тип интеграции со службой доставки
    """
    approve_comment: Optional[str] = Field(
        None, description="Комментарий при подтверждении заявки."
    )
    approve_date: Optional[datetime.datetime] = Field(
        None, description="Дата подтверждения заявки."
    )
    auto_approve_date: Optional[datetime.datetime] = Field(
        None, description="Дата автоматического подтверждения заявки."
    )
    cancellation_id: Optional[int] = Field(
        None, description="Идентификатор заявки на отмену."
    )
    cancellation_initiator: Optional[str] = Field(
        None, description="Инициатор отмены."
    )
    cancellation_reason: Optional[ConditionalCancellationReason] = Field(
        None, description="Причина отмены."
    )
    cancellation_reason_message: Optional[str] = Field(
        None, description="Комментарий к причине отмены."
    )
    cancelled_at: Optional[datetime.datetime] = Field(
        None, description="Дата создания заявки на отмену."
    )
    order_date: Optional[datetime.datetime] = Field(
        None, description="Дата оформления заказа."
    )
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    source_id: Optional[int] = Field(
        None, description="Идентификатор источника отмены."
    )
    state: Optional[ConditionalCancellationState] = Field(
        None, description="Статус заявки на отмену."
    )
    tpl_integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )


class ConditionalCancellationListResponse(BaseModel):
    """Ответ со списком заявок на отмену rFBS.

    Attributes:
        counter: Счётчики заявок по статусам
        last_id: Идентификатор последнего значения для пагинации
        result: Список заявок на отмену
    """
    counter: Optional[int] = Field(None, description="Счётчики заявок по статусам.")
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    result: Optional[list[ConditionalCancellationItem]] = Field(
        None, description="Список заявок на отмену."
    )
