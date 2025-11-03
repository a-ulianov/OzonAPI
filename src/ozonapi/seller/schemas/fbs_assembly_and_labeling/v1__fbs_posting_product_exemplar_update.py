"""https://docs.ozon.com/api/seller/?#operation/PostingAPI_FbsPostingProductExemplarUpdate"""
from pydantic import BaseModel, Field


class FBSPostingProductExemplarUpdateRequest(BaseModel):
    """Описывает схему запроса на обновление данных экземпляров.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )

class FBSPostingProductExemplarUpdateResponse(BaseModel):
    """Описывает схему ответа на запрос на обновление данных экземпляров."""
    pass