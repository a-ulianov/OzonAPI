"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_PostingMultiBoxQtySetV3"""
from pydantic import BaseModel, Field


class PostingFBSMultiBoxQtySetRequest(BaseModel):
    """Описывает запрос на указание количества коробок для многокоробочных отправлений.

    Attributes:
        posting_number: Идентификатор многокоробочного отправления
        multi_box_qty: Количество коробок, в которые упакован товар
    """

    posting_number: str = Field(
        ..., description="Идентификатор многокоробочного отправления."
    )
    multi_box_qty: int = Field(
        ..., description="Количество коробок, в которые упакован товар."
    )


class PostingFBSMultiBoxQtySetResult(BaseModel):
    """Описывает результат выполнения запроса на указание количества коробок для многокоробочных отправлений

    Attributes:
        result: Результат передачи количества коробок
    """
    result: bool = Field(
        ..., description="Результат передачи количества коробок."
    )


class PostingFBSMultiBoxQtySetResponse(BaseModel):
    """Описывает ответ на запрос на указание количества коробок для многокоробочных отправлений.

    Attributes:
        result: Описывает объект ответа на запрос на указание количества коробок для многокоробочных отправлений
    """
    result: PostingFBSMultiBoxQtySetResult = Field(
        ..., description="Описывает объект ответа на запрос на указание количества коробок для многокоробочных отправлений."
    )
