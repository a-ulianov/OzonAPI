import datetime
from typing import Optional

from pydantic import Field, BaseModel

from .product import PostingProduct
from .analytics_data import PostingAnalyticsData
from ....common.enumerations.postings import PostingStatus
from ...entities.postings import PostingFinancialData, PostingLegalInfo


class Posting(BaseModel):
    """Информация об отправлении.

    Attributes:
        analytics_data: Данные аналитики
        financial_data: Данные о стоимости товара
        in_process_at: Дата и время начала обработки отправления
        legal_info: Юридическая информация о покупателе
        order_id: Идентификатор заказа
        order_number: Номер заказа
        posting_number: Номер отправления
        products: Список товаров в отправлении
        status: Статус отправления
    """
    analytics_data: Optional[PostingAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    financial_data: Optional[PostingFinancialData] = Field(
        None, description="Данные о стоимости товара, размере скидки, выплате и комиссии."
    )
    in_process_at: datetime.datetime = Field(
        ..., description="Дата и время начала обработки отправления."
    )
    legal_info: Optional[PostingLegalInfo] = Field(
        None, description="Юридическая информация о покупателе."
    )
    order_id: int = Field(
        ..., description="Идентификатор заказа, к которому относится отправление."
    )
    order_number: str = Field(
        ..., description="Номер заказа, к которому относится отправление."
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[PostingProduct] = Field(
        ..., description="Список товаров в отправлении."
    )
    status: PostingStatus = Field(
        ..., description="Статус отправления."
    )
