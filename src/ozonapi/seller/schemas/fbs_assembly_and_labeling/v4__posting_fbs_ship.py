"""https://docs.ozon.com/api/seller/?#operation/PostingAPI_ShipFbsPostingV4"""
from typing import Optional

from pydantic import BaseModel, Field

from ..entities.postings.product import PostingProductWithCurrencyCode


class PostingFBSShipProduct(BaseModel):
    """Описывает схему товара.

    Attributes:
        product_id: Идентификатор товара в системе Ozon — SKU
        quantity: Количество экземпляров
    """
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    quantity: int = Field(
        ..., description="Количество экземпляров."
    )


class PostingFBSShipProducts(BaseModel):
    """Список товаров в отправлении.

    Attributes:
        products: Список товаров в отправлении
    """
    products: list[PostingFBSShipProduct] = Field(
        ..., description="Список товаров в отправлении."
    )


class PostingFBSShipRequestWith(BaseModel):
    """Описывает схему запроса дополнительной информации.

    Attributes:
        additional_data: Чтобы получить дополнительную информацию, передайте true.
    """
    additional_data: Optional[bool] = Field(
        True, description="Признак необходимости получения дополнительной информации в ответе."
    )


class PostingFBSShipRequest(BaseModel):
    """Описывает схему запроса на деление заказа на отправления и переводит его в статус `awaiting_deliver`.

    Attributes:
        packages: Список упаковок (каждая упаковка содержит список отправлений, на которые делится заказ)
        posting_number: Номер отправления
        with_: Дополнительная информация
    """
    model_config = {'populate_by_name': True}

    packages: list[PostingFBSShipProducts] = Field(
        ..., description="Список упаковок (каждая упаковка содержит список отправлений, на которые делится заказ)."
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    with_: Optional[PostingFBSShipRequestWith] = Field(
        default_factory=PostingFBSShipRequestWith, description="Дополнительная информация.",
        alias="with"
    )


class PostingFBSShipResponseProduct(PostingProductWithCurrencyCode):
    """Информация о товаре в отправлении.

    Attributes:
        mandatory_mark: Обязательная маркировка «Честный ЗНАК»
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
        currency_code: Валюта цен
    """
    mandatory_mark: Optional[list[str]] = Field(
        default_factory=list, description="Обязательная маркировка «Честный ЗНАК»."
    )


class PostingFBSShipPosting(BaseModel):
    """Описывает отправление.

    Attributes:
        posting_number: Номер отправления
        products: Список товаров в отправлении
    """
    posting_number: str = Field()
    products: Optional[list[PostingFBSShipResponseProduct]] = Field(
        default_factory=list, description="Список товаров в отправлении"
    )



class PostingFBSShipResponse(BaseModel):
    """Описывает схему ответа на запрос о делении заказа на отправления.

    Attributes:
        additional_data: Дополнительная информация об отправлениях
        result: Результат сборки отправлений
    """
    additional_data: Optional[list[PostingFBSShipPosting]] = Field(
        default_factory=list, description="Дополнительная информация об отправлениях."
    )
    result: list[str] = Field(
        ..., description="Результат сборки отправлений."
    )