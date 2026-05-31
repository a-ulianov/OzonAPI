"""https://docs.ozon.ru/api/seller/#operation/Review_InfoV2"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ReviewPhoto, ReviewVideo


class ReviewInfoRequest(BaseModel):
    """Описывает схему запроса на получение информации об отзыве.

    Attributes:
        review_id: Идентификатор отзыва
    """
    review_id: str = Field(
        ..., description="Идентификатор отзыва."
    )


class ReviewInfoResponse(BaseModel):
    """Описывает схему ответа на запрос информации об отзыве.

    Attributes:
        id: Идентификатор отзыва
        sku: Идентификатор товара в системе Ozon — SKU
        text: Текст отзыва
        rating: Оценка отзыва
        status: Статус отзыва
        order_status: Статус заказа
        published_at: Дата публикации отзыва
        is_rating_participant: Признак участия отзыва в подсчёте рейтинга
        comments_amount: Количество комментариев к отзыву
        likes_amount: Количество лайков на отзыве
        dislikes_amount: Количество дизлайков на отзыве
        photos: Информация об изображениях
        photos_amount: Количество изображений у отзыва
        videos: Информация о видео
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
        None, description="Количество комментариев к отзыву."
    )
    likes_amount: Optional[int] = Field(
        None, description="Количество лайков на отзыве."
    )
    dislikes_amount: Optional[int] = Field(
        None, description="Количество дизлайков на отзыве."
    )
    photos: Optional[list[ReviewPhoto]] = Field(
        None, description="Информация об изображениях."
    )
    photos_amount: Optional[int] = Field(
        None, description="Количество изображений у отзыва."
    )
    videos: Optional[list[ReviewVideo]] = Field(
        None, description="Информация о видео."
    )
    videos_amount: Optional[int] = Field(
        None, description="Количество видео у отзыва."
    )
