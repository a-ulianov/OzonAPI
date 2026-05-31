"""https://docs.ozon.ru/api/seller/#operation/Review_CommentList"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCommentListFilter(BaseModel):
    """Фильтр для получения списка комментариев к отзыву.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        published_from: Начало периода публикации
        published_to: Конец периода публикации
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    published_from: Optional[str] = Field(
        None, description="Начало периода публикации."
    )
    published_to: Optional[str] = Field(
        None, description="Конец периода публикации."
    )


class ReviewCommentListRequest(BaseModel):
    """Описывает схему запроса на получение списка комментариев к отзыву.

    Attributes:
        limit: Ограничение значений в ответе
        review_id: Идентификатор отзыва
        offset: Количество пропускаемых элементов
        sort_dir: Направление сортировки (`ASC` / `DESC`)
        filter: Фильтр для поиска комментариев
    """
    limit: int = Field(
        ..., description="Ограничение значений в ответе."
    )
    review_id: Optional[str] = Field(
        None, description="Идентификатор отзыва."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )
    filter: Optional[ReviewCommentListFilter] = Field(
        None, description="Фильтр для поиска комментариев."
    )


class ReviewCommentListComment(BaseModel):
    """Комментарий к отзыву.

    Attributes:
        id: Идентификатор комментария
        text: Текст комментария
        parent_comment_id: Идентификатор родительского комментария
        published_at: Дата публикации комментария
        is_official: Признак официального комментария
        is_owner: Признак комментария продавца
        is_published: Признак публикации комментария
        is_rejected: Признак отклонения комментария
        deviation_reason: Причина отклонения на модерации
        likes_amount: Количество лайков
        dislikes_amount: Количество дизлайков
    """
    id: Optional[str] = Field(
        None, description="Идентификатор комментария."
    )
    text: Optional[str] = Field(
        None, description="Текст комментария."
    )
    parent_comment_id: Optional[str] = Field(
        None, description="Идентификатор родительского комментария."
    )
    published_at: Optional[str] = Field(
        None, description="Дата публикации комментария."
    )
    is_official: Optional[bool] = Field(
        None, description="`true`, если комментарий оставило официальное лицо."
    )
    is_owner: Optional[bool] = Field(
        None, description="`true`, если комментарий оставил продавец."
    )
    is_published: Optional[bool] = Field(
        None, description="`true`, если комментарий опубликован."
    )
    is_rejected: Optional[bool] = Field(
        None, description="`true`, если комментарий отклонён."
    )
    deviation_reason: Optional[str] = Field(
        None, description="Причина отклонения на модерации."
    )
    likes_amount: Optional[int] = Field(
        None, description="Количество лайков."
    )
    dislikes_amount: Optional[int] = Field(
        None, description="Количество дизлайков."
    )


class ReviewCommentListResponse(BaseModel):
    """Описывает схему ответа на запрос списка комментариев к отзыву.

    Attributes:
        comments: Информация о комментариях
        offset: Количество элементов в выдаче
    """
    comments: Optional[list[ReviewCommentListComment]] = Field(
        None, description="Информация о комментариях."
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов в выдаче."
    )
