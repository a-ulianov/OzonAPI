from typing import Optional

from pydantic import Field

from src.ozonapi.seller.schemas.entities.postings import PostingAnalyticsData


class PostingFBOAnalyticsData(PostingAnalyticsData):
    """Данные аналитики.

    Attributes:
        city: Город доставки
        delivery_type: Способ доставки
        is_legal: Признак юридического лица
        is_premium: Наличие подписки Premium
        payment_type_group_name: Способ оплаты
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада отправки заказа
    """
    warehouse_name: Optional[str] = Field(
        None, description="Название склада отправки заказа."
    )
