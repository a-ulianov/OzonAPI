"""Схемы метода receipts_upload (загрузить чек, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.receipts import ReceiptType


class ReceiptsUploadRequest(BaseModel):
    """Параметры запроса загрузки чека.

    Notes:
        • Запрос отправляется как `multipart/form-data`.

    Attributes:
        content: Содержимое файла чека в бинарном виде
        operation_type: Тип операции (значение из `receipts_seller_list()`)
        posting_numbers: Номера отправлений
        receipt_number: Номер чека
        type: Тип чека (`INCOMING` — реализации, `REFUND` — возврата)
        parent_receipt_id: Идентификатор родительского чека (для изменения чека)
    """
    content: bytes = Field(..., description="Содержимое файла чека в бинарном виде.")
    operation_type: str = Field(
        ...,
        description="Тип операции. Получите значение методом `receipts_seller_list()`."
    )
    posting_numbers: list[str] = Field(..., description="Номера отправлений.")
    receipt_number: str = Field(..., description="Номер чека.")
    type: ReceiptType = Field(
        ..., description="Тип чека: `INCOMING` — реализации, `REFUND` — возврата."
    )
    parent_receipt_id: Optional[str] = Field(
        None,
        description="Идентификатор родительского чека. Передайте идентификатор чека, "
                    "который нужно изменить."
    )


class ReceiptsUploadResponse(BaseModel):
    """Ответ на загрузку чека.

    Attributes:
        receipt_id: Идентификатор чека
    """
    receipt_id: str = Field("", description="Идентификатор чека.")
