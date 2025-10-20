"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_ChangeFbsPostingProduct"""
from pydantic import BaseModel, Field


class PostingFBSProductChangeRequestItem(BaseModel):
    """Информация о товарах.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        weight_real: Вес единиц товара в отправлении
    """
    model_config = {'populate_by_name': True}

    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    weight_real: float = Field(
        ..., description="Вес единиц товара в отправлении.",
        alias="weightReal"
    )


class PostingFBSProductChangeRequest(BaseModel):
    """Описывает схему запроса на добавление веса для весовых товаров в отправлении.

    Attributes:
        items: Информация о товарах
        posting_number: Идентификатор отправления
    """
    items: list[PostingFBSProductChangeRequestItem] = Field(
        ..., description="Информация о товарах."
    )
    posting_number: str = Field(
        ..., description="Идентификатор отправления."
    )


class PostingFBSProductChangeResponse(BaseModel):
    """Описывает схему ответа на запрос на добавление веса для весовых товаров в отправлении.

    Attributes:
        result: Идентификатор отправления
    """
    result: str = Field(
        ..., description="Идентификатор отправления."
    )
