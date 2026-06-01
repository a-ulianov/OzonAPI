"""Схемы метода receipts_get (получить чек в формате PDF, v1)."""
from pydantic import BaseModel, Field


class ReceiptsGetRequest(BaseModel):
    """Параметры запроса чека.

    Attributes:
        receipt_id: Идентификатор чека
    """
    receipt_id: str = Field(
        ...,
        description="Идентификатор чека. Получите его методом `receipts_seller_list()`."
    )


class ReceiptsGetResponse(BaseModel):
    """Ответ с чеком в формате PDF.

    Notes:
        • API возвращает JSON с полем `content` — содержимым PDF-файла в виде
          строки (base64).

    Attributes:
        content: PDF-файл с чеком в виде строки base64
    """
    content: str = Field("", description="PDF-файл с чеком в виде строки base64.")
