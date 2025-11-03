"""https://docs.ozon.com/api/seller/?#operation/PostingAPI_ShipFbsPostingPackage"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSShipPackageProduct(BaseModel):
    """Описывает товар в отправлении.

    Attributes:
        exemplars_ids: Идентификаторы экземпляров товара
        product_id: Идентификатор товара в системе продавца — SKU
        quantity: Кол-во экземпляров
    """
    model_config = {'populate_by_name': True}

    exemplars_ids: Optional[list[str]] = Field(
        default_factory=list, description="Идентификаторы экземпляров товара.",
        alias="exemplarsIds",
    )
    product_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — SKU."
    )
    quantity: int = Field(
        ..., description="Кол-во экземпляров."
    )


class PostingFBSShipPackageRequest(BaseModel):
    """Описывает схему запроса на частичную сборку отправления.

    Attributes:
        posting_number: Номер отправления
        products: Список товаров в отправлении
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[PostingFBSShipPackageProduct] = Field(
        ..., description="Список товаров в отправлении."
    )


class PostingFBSShipPackageResponse(BaseModel):
    """Описывает схему ответа на запрос о частичной сборке отправления.

    Attributes:
        result: Номера отправлений, сформированные после сборки
    """
    result: str = Field(
        ..., description="Номера отправлений, сформированные после сборки."
    )