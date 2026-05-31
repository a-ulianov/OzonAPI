"""https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutList"""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnGiveoutListRequest(BaseModel):
    """Описывает схему запроса на получение списка возвратных отгрузок.

    Attributes:
        limit: Количество элементов в ответе
        last_id: Идентификатор последнего значения на странице
    """
    limit: int = Field(
        ..., description="Количество элементов в ответе."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения на странице."
    )


class ReturnGiveoutListItem(BaseModel):
    """Информация о возвратной отгрузке.

    Attributes:
        giveout_id: Идентификатор отгрузки
        giveout_status: Статус отгрузки
        approved_articles_count: Количество товаров в отгрузке
        total_articles_count: Общее количество товаров, которые нужно забрать
        created_at: Дата и время создания
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
        warehouse_address: Адрес склада
    """
    giveout_id: Optional[int] = Field(
        None, description="Идентификатор отгрузки."
    )
    giveout_status: Optional[str] = Field(
        None, description="Статус отгрузки."
    )
    approved_articles_count: Optional[int] = Field(
        None, description="Количество товаров в отгрузке."
    )
    total_articles_count: Optional[int] = Field(
        None, description="Общее количество товаров, которые нужно забрать."
    )
    created_at: Optional[str] = Field(
        None, description="Дата и время создания."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
    warehouse_name: Optional[str] = Field(
        None, description="Название склада."
    )
    warehouse_address: Optional[str] = Field(
        None, description="Адрес склада."
    )


class ReturnGiveoutListResponse(BaseModel):
    """Описывает схему ответа на запрос списка возвратных отгрузок.

    Attributes:
        giveouts: Список возвратных отгрузок
    """
    giveouts: Optional[list[ReturnGiveoutListItem]] = Field(
        None, description="Список возвратных отгрузок."
    )
