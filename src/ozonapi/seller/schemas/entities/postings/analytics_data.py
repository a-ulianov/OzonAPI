from typing import Optional

from pydantic import BaseModel, Field

from ....common.enumerations.postings import PaymentTypeGroupName


class PostingAnalyticsData(BaseModel):
    """Данные аналитики.

    Attributes:
        city: Город доставки
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