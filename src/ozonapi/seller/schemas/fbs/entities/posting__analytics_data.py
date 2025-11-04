import datetime
from typing import Optional

from pydantic import Field

from ...entities.postings import PostingAnalyticsData


class PostingFBSAnalyticsData(PostingAnalyticsData):
    """Данные аналитики.

    Attributes:
        city: Город доставки
        delivery_date_begin: Дата и время начала доставки
        delivery_date_end: Дата и время конца доставки
        delivery_type: Способ доставки
        is_legal: Признак юридического лица
        is_premium: Наличие подписки Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада отправки заказа
        warehouse_id: Идентификатор склада
    """
    delivery_date_begin: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала доставки."
    )
    delivery_date_end: Optional[datetime.datetime] = Field(
        None, description="Дата и время конца доставки."
    )
    region: Optional[str] = Field(
        ..., description="Регион доставки. Только для отправлений rFBS."
    )
    tpl_provider: str = Field(
        ..., description="Служба доставки."
    )
    tpl_provider_id: int = Field(
        ..., description="Идентификатор службы доставки."
    )
    warehouse: str = Field(
        ..., description="Название склада отправки заказа."
    )
