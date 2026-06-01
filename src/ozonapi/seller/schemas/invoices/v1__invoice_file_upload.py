"""Схемы метода invoice_file_upload (загрузка счёта-фактуры, v1)."""
from pydantic import BaseModel, Field


class InvoiceFileUploadRequest(BaseModel):
    """Параметры запроса загрузки счёта-фактуры.

    Attributes:
        base64_content: Счёт-фактура в кодировке Base64
        posting_number: Номер отправления
    """
    base64_content: str = Field(..., description="Счёт-фактура в кодировке Base64.")
    posting_number: str = Field(..., description="Номер отправления.")


class InvoiceFileUploadResponse(BaseModel):
    """Ответ на загрузку счёта-фактуры.

    Attributes:
        url: Ссылка на загруженный счёт-фактуру
    """
    url: str = Field("", description="Ссылка на загруженный счёт-фактуру.")
