"""https://docs.ozon.ru/api/seller/#operation/Review_List"""
from typing import Optional

from pydantic import BaseModel, Field

from .v2__review_list import ReviewListResponse


class ReviewListV1Request(BaseModel):
    """Описывает схему запроса на получение списка отзывов (v1).

    Attributes:
        limit: Количество отзывов в ответе
        last_id: Идентификатор последнего отзыва на странице
        sort_dir: Направление сортировки (`ASC` / `DESC`)
        status: Статус отзывов (`ALL`, `UNPROCESSED`, `PROCESSED`)
    """
    limit: int = Field(
        ..., description="Количество отзывов в ответе."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего отзыва на странице."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )
    status: Optional[str] = Field(
        None, description="Статусы отзывов: `ALL` — все, `UNPROCESSED` — необработанные, `PROCESSED` — обработанные."
    )


class ReviewListV1Response(ReviewListResponse):
    """Описывает схему ответа на запрос списка отзывов (v1).

    Notes:
        • Схема ответа идентична версии v2 (`ReviewListResponse`).
    """
    pass
