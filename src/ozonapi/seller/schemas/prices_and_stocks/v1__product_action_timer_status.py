"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductActionTimerStatus"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductActionTimerStatusRequest(BaseModel):
    """Схема запроса на получение статуса таймера актуальности минимальной цены.

    Attributes:
        product_ids: Список идентификаторов товаров в системе Ozon — product_id (максимум 1000)
    """
    product_ids: list[str] = Field(
        ..., description="Список идентификаторов товаров в системе Ozon — product_id.",
        min_length=1, max_length=1000
    )


class ProductActionTimerStatus(BaseModel):
    """Схема статуса таймера актуальности минимальной цены товара.

    Attributes:
        expired_at: Время окончания таймера (если пусто — активного таймера нет)
        min_price_for_auto_actions_enabled: Признак учёта минимальной цены при добавлении в акции
        product_id: Идентификатор товара в системе Ozon — product_id
    """
    expired_at: Optional[datetime.datetime] = Field(
        None, description="Время окончания таймера. Если параметр пустой, активного таймера нет."
    )
    min_price_for_auto_actions_enabled: bool = Field(
        ..., description="true, если Ozon учитывает минимальную цену при добавлении товара в акции."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon — product_id."
    )


class ProductActionTimerStatusResponse(BaseModel):
    """Схема ответа на запрос статуса таймера актуальности минимальной цены.

    Attributes:
        statuses: Список статусов таймеров по запрошенным товарам
    """
    statuses: list[ProductActionTimerStatus] = Field(
        ..., description="Список статусов таймеров по запрошенным товарам."
    )
