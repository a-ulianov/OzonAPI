"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_MoveFbsPostingToArbitration"""
from pydantic import BaseModel, Field


class PostingFBSArbitrationRequest(BaseModel):
    """Описывает схему запроса на открытие спора по отправлениям.

    Attributes:
        posting_number: Список идентификаторов отправлений
    """
    posting_number: list[str] = Field(
        ..., description="Список идентификаторов отправлений."
    )

class PostingFBSArbitrationResponse(BaseModel):
    """Описывает схему ответа на запрос об открытии спора по отправлениям.

    Attributes:
        result: Результат обработки запроса (true, если запрос выполнился без ошибок)
    """
    result: bool = Field(
        ..., description="Результат обработки запроса (true, если запрос выполнился без ошибок)."
    )