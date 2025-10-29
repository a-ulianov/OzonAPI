"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarCreateOrGetV6"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingProduct


class FBSPostingProductExemplarCreateOrGetRequest(BaseModel):
    """Описывает схему запроса на получение информации о созданных экземплярах (кол-во коробок, список товаров).

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )

class FBSPostingProductExemplarCreateOrGetResponse(BaseModel):
    """Описывает схему ответа на запрос о созданных экземплярах.

    Attributes:
        multi_box_qty: Количество коробок, в которые упакован товар
        posting_number: Номер отправления
        products: Список товаров
    """
    multi_box_qty: int = Field(
        ..., description="Количество коробок, в которые упакован товар."
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: Optional[list[PostingProduct]] = Field(
        default_factory=list, description="Список товаров."
    )