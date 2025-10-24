"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPostingProduct"""
from pydantic import BaseModel, Field


class PostingFBSProductCancelItem(BaseModel):
    """Информация о товаре и их количестве.

    Attributes:
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon — SKU
    """
    quantity: int = Field(
        ..., description="Количество товара в отправлении."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU"
    )


class PostingFBSProductCancelRequest(BaseModel):
    """Описывает схему запроса на отмену отправки некоторых товаров в отправлении.

    Attributes:
        cancel_reason_id: Идентификатор причины отмены отправления товара (можно получить методом `posting_fbs_cancel_reason_list()`)
        cancel_reason_message: Дополнительная информация по отмене
        items: Информация о товарах и их количестве
        posting_number: Идентификатор отправления
    """
    cancel_reason_id: int = Field(
        ..., description="Идентификатор причины отмены отправления товара (можно получить методом `posting_fbs_cancel_reason_list()`)."
    )
    cancel_reason_message: str = Field(
        ..., description="Дополнительная информация по отмене. Обязательное поле."
    )
    items: list[PostingFBSProductCancelItem] = Field(
        ..., description="Информация о товарах и их количестве."
    )
    posting_number: str = Field(
        ..., description="Идентификатор отправления"
    )


class PostingFBSProductCancelResponse(BaseModel):
    """Описывает схему ответа на запрос об отмене отправки некоторых товаров в отправлении.

    Attributes:
        result: Номер отправления
    """
    result: str = Field(
        ..., description="Номер отправления."
    )