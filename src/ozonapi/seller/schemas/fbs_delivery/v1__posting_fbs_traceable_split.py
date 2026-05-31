"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFbsTraceableSplit"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSTraceableSplitRequest(BaseModel):
    """Описывает схему запроса на разделение отправления с прослеживаемыми товарами.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )


class PostingFBSTraceableSplitProduct(BaseModel):
    """Товар в отправлении после разделения.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        quantity: Количество
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    quantity: Optional[int] = Field(
        None, description="Количество."
    )


class PostingFBSTraceableSplitResponsePosting(BaseModel):
    """Информация об отправлении после разделения.

    Attributes:
        posting_number: Номер отправления
        potential_blr_traceable: Признак потенциально прослеживаемого товара
        products: Список товаров в отправлении
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    potential_blr_traceable: Optional[bool] = Field(
        None, description="Признак, что товар потенциально прослеживаемый."
    )
    products: Optional[list[PostingFBSTraceableSplitProduct]] = Field(
        None, description="Список товаров в отправлении."
    )


class PostingFBSTraceableSplitResponse(BaseModel):
    """Описывает схему ответа на запрос разделения отправления с прослеживаемыми товарами.

    Attributes:
        postings: Информация об отправлениях
    """
    postings: Optional[list[PostingFBSTraceableSplitResponsePosting]] = Field(
        None, description="Информация об отправлениях."
    )
