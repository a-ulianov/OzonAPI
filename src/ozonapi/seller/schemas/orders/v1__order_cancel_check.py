"""Схемы метода order_cancel_check (проверка возможности отмены заказа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class OrderCancelCheckRequest(BaseModel):
    """Параметры запроса проверки возможности отмены заказа.

    Attributes:
        order_number: Номер заказа
    """
    order_number: str = Field(..., description="Номер заказа.")


class OrderCancelCheckPostingGroup(BaseModel):
    """Группа отправлений заказа.

    Attributes:
        posting_numbers: Номера отправлений в группе
    """
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений в группе."
    )


class OrderCancelCheckPosting(BaseModel):
    """Возможность отмены отдельного отправления.

    Attributes:
        cancellable: Отправление можно отменить
        posting_number: Номер отправления
        why_not_cancellable: Причина невозможности отмены
    """
    cancellable: Optional[bool] = Field(
        None, description="Отправление можно отменить."
    )
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    why_not_cancellable: Optional[str] = Field(
        None, description="Причина невозможности отмены."
    )


class OrderCancelCheckResponse(BaseModel):
    """Ответ с информацией о возможности отмены заказа.

    Attributes:
        cancellable: Заказ можно отменить
        order_number: Номер заказа
        posting_groups: Группы отправлений заказа
        postings: Отправления заказа
    """
    cancellable: Optional[bool] = Field(None, description="Заказ можно отменить.")
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    posting_groups: Optional[list[OrderCancelCheckPostingGroup]] = Field(
        None, description="Группы отправлений заказа."
    )
    postings: Optional[list[OrderCancelCheckPosting]] = Field(
        None, description="Отправления заказа."
    )
