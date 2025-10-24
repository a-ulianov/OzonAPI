"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_MoveFbsPostingToArbitration"""
from pydantic import BaseModel, Field


class PostingFBSAwaitingDeliveryRequest(BaseModel):
    """Описывает схему запроса на передачу отправлений к отгрузке.

    Attributes:
        posting_number: Идентификатор отправления (максимальное количество в одном запросе — 100)
    """
    posting_number: list[str] = Field(
        ..., description="Идентификатор отправления (максимальное количество в одном запросе — 100).",
        max_length=100,
    )

class PostingFBSAwaitingDeliveryResponse(BaseModel):
    """Описывает схему ответа на запрос о передаче отправлений к отгрузке.

    Attributes:
        result: Результат обработки запроса (true, если запрос выполнился без ошибок)
    """
    result: bool = Field(
        ..., description="Результат обработки запроса (true, если запрос выполнился без ошибок)."
    )