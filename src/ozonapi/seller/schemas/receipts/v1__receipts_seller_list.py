"""Схемы метода receipts_seller_list (список чеков продавца, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.receipts import ReceiptOperationType, ReceiptType


class ReceiptsSellerListRequest(BaseModel):
    """Параметры запроса списка чеков продавца.

    Attributes:
        page: Номер страницы
        page_size: Количество элементов на странице
        posting_numbers: Номера отправлений
    """
    page: Optional[int] = Field(None, description="Номер страницы.")
    page_size: Optional[int] = Field(
        None, description="Количество элементов на странице."
    )
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )


class ReceiptsSellerListReceipt(BaseModel):
    """Чек продавца.

    Attributes:
        created_at: Дата создания чека
        operation_type: Тип операции
        order_id: Идентификатор заказа
        parent_receipt_id: Идентификатор родительского чека
        posting_numbers: Номера отправлений
        receipt_id: Идентификатор чека
        receipt_number: Номер чека
        type: Тип чека
        updated_at: Дата обновления чека
    """
    created_at: Optional[str] = Field(None, description="Дата создания чека.")
    operation_type: Optional[ReceiptOperationType] = Field(
        None, description="Тип операции."
    )
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    parent_receipt_id: Optional[str] = Field(
        None, description="Идентификатор родительского чека."
    )
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )
    receipt_id: Optional[str] = Field(None, description="Идентификатор чека.")
    receipt_number: Optional[str] = Field(None, description="Номер чека.")
    type: Optional[ReceiptType] = Field(None, description="Тип чека.")
    updated_at: Optional[str] = Field(None, description="Дата обновления чека.")


class ReceiptsSellerListResponse(BaseModel):
    """Ответ со списком чеков продавца.

    Attributes:
        has_next: Признак наличия следующей страницы
        receipts: Список чеков
    """
    has_next: bool = Field(False, description="Признак наличия следующей страницы.")
    receipts: list[ReceiptsSellerListReceipt] = Field(
        default_factory=list, description="Список чеков."
    )
