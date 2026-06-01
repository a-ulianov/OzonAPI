"""Схемы метода invoice_delete (удаление ссылки на счёт-фактуру, v1)."""
from pydantic import BaseModel, Field


class InvoiceDeleteRequest(BaseModel):
    """Параметры запроса удаления ссылки на счёт-фактуру.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(..., description="Номер отправления.")


class InvoiceDeleteResponse(BaseModel):
    """Ответ на удаление ссылки на счёт-фактуру.

    Attributes:
        result: Результат обработки запроса — `true`, если успешно
    """
    result: bool = Field(False, description="Результат обработки запроса.")
