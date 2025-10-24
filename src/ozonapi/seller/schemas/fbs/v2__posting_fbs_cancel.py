"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPosting"""
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class PostingFBSCancelRequest(BaseModel):
    """Описывает схему запроса на отмену отправления.

    Attributes:
        cancel_reason_id: Идентификатор причины отмены отправления товара (можно получить методом `posting_fbs_cancel_reason_list()`)
        cancel_reason_message: Дополнительная информация по отмене (опционально, если cancel_reason_id = 402, параметр обязательный)
        posting_number: Идентификатор отправления
    """
    cancel_reason_id: int = Field(
        ..., description="Идентификатор причины отмены отправления товара (можно получить методом `posting_fbs_cancel_reason_list()`)."
    )
    cancel_reason_message: Optional[str] = Field(
        None, description="Дополнительная информация по отмене (если cancel_reason_id = 402, параметр обязательный)."
    )
    posting_number: str = Field(
        ..., description="Идентификатор отправления."
    )

    @model_validator(mode='after')
    def validate_reason_message(self) -> 'PostingFBSCancelRequest':
         if self.cancel_reason_id == 402 and self.cancel_reason_message is None:
            raise ValueError(
                "При cancel_reason_id = 402, параметр cancel_reason_message обязательный."
            )
         return self


class PostingFBSCancelResponse(BaseModel):
    """Описывает схему ответа на запрос об отмене отправления.

    Attributes:
        result: Результат обработки запроса (true, если запрос выполнился без ошибок)
    """
    result: bool = Field(
        ..., description="Результат обработки запроса (true, если запрос выполнился без ошибок)."
    )