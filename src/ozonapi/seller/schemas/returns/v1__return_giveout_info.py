"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutInfo"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutInfoRequest(BaseModel):
    """Описывает схему запроса на получение информации о возвратной отгрузке.

    Attributes:
        giveout_id: Идентификатор отгрузки
    """
    giveout_id: int = Field(
        ..., description="Идентификатор отгрузки."
    )


class ReturnGiveoutInfoArticle(BaseModel):
    """Артикул товара в возвратной отгрузке.

    Attributes:
        name: Название товара
        seller_id: Идентификатор продавца
        approved: Признак подтверждения отгрузки
        delivery_schema: Схема доставки
    """
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    seller_id: Optional[int] = Field(
        None, description="Идентификатор продавца."
    )
    approved: Optional[bool] = Field(
        None, description="`true`, если отгрузка подтверждена."
    )
    delivery_schema: Optional[str] = Field(
        None, description="Схема доставки."
    )


class ReturnGiveoutInfoResponse(BaseModel):
    """Описывает схему ответа на запрос информации о возвратной отгрузке.

    Attributes:
        giveout_id: Идентификатор отгрузки
        giveout_status: Статус отгрузки
        articles: Артикулы товаров
        warehouse_name: Название склада
        warehouse_address: Адрес склада
    """
    giveout_id: Optional[int] = Field(
        None, description="Идентификатор отгрузки."
    )
    giveout_status: Optional[str] = Field(
        None, description="Статус отгрузки."
    )
    articles: Optional[list[ReturnGiveoutInfoArticle]] = Field(
        None, description="Артикулы товаров."
    )
    warehouse_name: Optional[str] = Field(
        None, description="Название склада."
    )
    warehouse_address: Optional[str] = Field(
        None, description="Адрес склада."
    )
