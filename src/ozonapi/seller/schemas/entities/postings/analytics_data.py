import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ....common.enumerations.postings import PaymentTypeGroupName


class PostingAnalyticsData(BaseModel):
    """Данные аналитики.

    Attributes:
        city: Город доставки
        client_delivery_date_begin: Дата и время начала доставки
        client_delivery_date_end: Ожидаемая дата, до которой заказ будет доставлен
        delivery_date_begin: Дата и время начала доставки
        delivery_date_end: Дата и время конца доставки
        delivery_type: Способ доставки
        is_legal: Признак юридического лица
        is_premium: Наличие подписки Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки
        warehouse_id: Идентификатор склада
    """
    city: Optional[str] = Field(
        ..., description="Город доставки. Только для отправлений rFBS и продавцов из СНГ."
    )
    client_delivery_date_begin: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала доставки."
    )
    client_delivery_date_end: Optional[datetime.datetime] = Field(
        None, description="Ожидаемая дата, до которой заказ будет доставлен."
    )
    delivery_date_begin: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала доставки."
    )
    delivery_date_end: Optional[datetime.datetime] = Field(
        None, description="Дата и время конца доставки."
    )
    delivery_type: Optional[str] = Field(
        None, description="Способ доставки."
    )
    is_legal: bool = Field(
        ..., description="Признак, что получатель юридическое лицо."
    )
    is_premium: bool = Field(
        ..., description="Наличие подписки Premium."
    )
    payment_type_group_name: PaymentTypeGroupName | str = Field(
        ..., description="Способ оплаты."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )