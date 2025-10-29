"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarStatusV5"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.postings import PostingShipmentStatus
from .entities import ProductExemplarChecked


class FBSPostingProductExemplarStatusRequest(BaseModel):
    """Описывает схему запроса на получение статуса добавления экземпляров.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )


class FBSPostingProductExemplarStatusProducts(BaseModel):
    """Описывает схему товара.

    Attributes:
        exemplars: Информация об экземплярах
        product_id: Идентификатор товара в системе
    """
    exemplars: Optional[list[ProductExemplarChecked]] = Field(
        default_factory=list, description="Информация об экземплярах."
    )
    product_id: str = Field(
        ..., description="Идентификатор товара в системе."
    )



class FBSPostingProductExemplarStatusResponse(BaseModel):
    """Описывает схему ответа на запрос о получении статуса добавления экземпляров.

    Attributes:
        posting_number: Номер отправления
        products: Список товаров
        status: Статус проверки всех экземпляров и доступности сборки
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[FBSPostingProductExemplarStatusProducts] = Field(
        default_factory=list, description="Список товаров."
    )
    status: Optional[PostingShipmentStatus | str] = Field(
        None, description="Статус проверки всех экземпляров и доступности сборки."
    )