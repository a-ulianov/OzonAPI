import datetime
from typing import Optional

from pydantic import Field

from ...entities.common import AdditionalData
from ...entities.postings import Posting
from .posting__analytics_data import PostingFBOAnalyticsData
from .posting__product import PostingFBOProduct


class PostingFBOPosting(Posting):
    """Описывает отправление.

    Attributes:
        additional_data: Дополнительная информация
        analytics_data: Данные аналитики
        cancel_reason_id: Идентификатор причины отмены отправления
        created_at: Дата и время создания отправления
        financial_data: Финансовые данные
        in_process_at: Дата и время начала обработки отправления
        legal_info: Юридическая информация о покупателе
        order_id: Идентификатор заказа, к которому относится отправление
        order_number: Номер заказа, к которому относится отправление
        posting_number: Номер отправления
        products: Список товаров в отправлении
        status: Статус отправления
    """
    additional_data: Optional[list[AdditionalData]] = Field(
        default_factory=list, description="Дополнительная информация."
    )
    analytics_data: Optional[PostingFBOAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены отправления."
    )
    created_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время создания отправления."
    )
    products: Optional[list[PostingFBOProduct]] = Field(
        default_factory=list, description="Список товаров в отправлении."
    )
