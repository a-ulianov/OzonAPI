"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_GetFbsPostingByBarcode"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingFBSBarcodes
from ..entities.postings.product import PostingProduct


class PostingFBSGetByBarcodeRequest(BaseModel):
    """Запрос на получение информации об отправлении по штрихкоду.

    Attributes:
        barcode: Штрихкод отправления (можно получить с помощью методов posting_fbs_get(), posting_fbs_list() и posting_fbs_unfulfilled_list() в массиве barcodes)
    """
    barcode: str = Field(
        ..., title="Штрихкод отправления (можно получить с помощью методов posting_fbs_get(), posting_fbs_list() и posting_fbs_unfulfilled_list() в массиве barcodes)."
    )


class PostingFBSGetByBarcodeResponse(BaseModel):
    """Описывает схему ответа на запрос на получение информации об отправлении по штрихкоду.

    Attributes:
        barcodes: Штрихкоды отправления
        cancel_reason_id: Идентификатор причины отмены отправления
        created_at: Дата и время создания отправления
        in_process_at: Дата и время начала обработки отправления
        order_id: Идентификатор заказа, к которому относится отправление
        order_number: Номер заказа, к которому относится отправление
        posting_number: Номер отправления
        products: Список товаров в отправлении
        shipment_date: Дата и время, до которой необходимо собрать отправление (если отправление не собрать к этой дате — оно автоматически отменится)
        status: Статус отправления
    """
    barcodes: PostingFBSBarcodes = Field(
        ..., description="Штрихкоды отправления"
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены отправления"
    )
    created_at: datetime.datetime = Field(
        ..., description="Дата и время создания отправления"
    )
    in_process_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала обработки отправления"
    )
    order_id: int = Field(
        ..., description="Идентификатор заказа, к которому относится отправление"
    )
    order_number: str = Field(
        ..., description="Номер заказа, к которому относится отправление"
    )
    posting_number: str = Field(
        ..., description="Номер отправления"
    )
    products: list[PostingProduct] = Field(
        ..., description="Список товаров в отправлении"
    )
    shipment_date: datetime.datetime = Field(
        ..., description="Дата и время, до которой необходимо собрать отправление (если отправление не собрать к этой дате — оно автоматически отменится)"
    )
    status: str = Field(
        ..., description="Статус отправления"
    )