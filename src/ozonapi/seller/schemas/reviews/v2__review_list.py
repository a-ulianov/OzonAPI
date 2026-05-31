"""https://docs.ozon.ru/api/seller/#operation/Review_ListV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewListFilters(BaseModel):
    """Фильтры для получения списка отзывов.

    Attributes:
        status: Статус отзыва
        order_status: Статус заказа
        skus: Идентификаторы товаров в системе Ozon — SKU
        published_from: Начало периода публикации
        published_to: Конец периода публикации
    """
    status: Optional[str] = Field(
        None, description="Статус отзыва."
    )
    order_status: Optional[str] = Field(
        None, description="Статус заказа."
    )
    skus: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    published_from: Optional[str] = Field(
        None, description="Начало периода публикации."
    )
    published_to: Optional[str] = Field(
        None, description="Конец периода публикации."
    )


class ReviewListRequest(BaseModel):
    """Описывает схему запроса на получение списка отзывов.

    Attributes:
        limit: Количество отзывов в ответе
        last_id: Идентификатор последнего отзыва на странице
        sort_dir: Направление сортировки (`ASC` / `DESC`)
        filters: Фильтры для поиска отзывов
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
    filters: Optional[ReviewListFilters] = Field(
        None, description="Фильтры для поиска отзывов."
    )


class ReviewListReview(BaseModel):
    """Отзыв в списке.

    Attributes:
        id: Идентификатор отзыва
        sku: Идентификатор товара в системе Ozon — SKU
        text: Текст отзыва
        rating: Оценка отзыва
        status: Статус отзыва
        order_status: Статус заказа
        published_at: Дата публикации отзыва
        is_rating_participant: Признак участия отзыва в подсчёте рейтинга
        comments_amount: Количество комментариев у отзыва
        photos_amount: Количество изображений у отзыва
        videos_amount: Количество видео у отзыва
    """
    id: Optional[str] = Field(
        None, description="Идентификатор отзыва."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    text: Optional[str] = Field(
        None, description="Текст отзыва."
    )
    rating: Optional[int] = Field(
        None, description="Оценка отзыва."
    )
    status: Optional[str] = Field(
        None, description="Статус отзыва."
    )
    order_status: Optional[str] = Field(
        None, description="Статус заказа, на который покупатель оставил отзыв."
    )
    published_at: Optional[str] = Field(
        None, description="Дата публикации отзыва."
    )
    is_rating_participant: Optional[bool] = Field(
        None, description="`true`, если отзыв участвует в подсчёте рейтинга."
    )
    comments_amount: Optional[int] = Field(
        None, description="Количество комментариев у отзыва."
    )
    photos_amount: Optional[int] = Field(
        None, description="Количество изображений у отзыва."
    )
    videos_amount: Optional[int] = Field(
        None, description="Количество видео у отзыва."
    )


class ReviewListResponse(BaseModel):
    """Описывает схему ответа на запрос списка отзывов.

    Attributes:
        reviews: Список отзывов
        has_next: Признак наличия следующей страницы
        last_id: Идентификатор последнего отзыва на странице
    """
    reviews: Optional[list[ReviewListReview]] = Field(
        None, description="Список отзывов."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если в ответе вернули не все отзывы."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего отзыва на странице."
    )
