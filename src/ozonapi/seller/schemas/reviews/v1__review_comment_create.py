"""https://docs.ozon.ru/api/seller/#operation/Review_CommentCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCommentCreateRequest(BaseModel):
    """Описывает схему запроса на создание комментария к отзыву.

    Attributes:
        review_id: Идентификатор отзыва
        text: Текст комментария
        mark_review_as_processed: Признак перевода отзыва в статус «Обработанный»
        parent_comment_id: Идентификатор родительского комментария
    """
    review_id: str = Field(
        ..., description="Идентификатор отзыва."
    )
    text: str = Field(
        ..., description="Текст комментария."
    )
    mark_review_as_processed: Optional[bool] = Field(
        None, description="`true`, если нужно перевести отзыв в статус «Обработанный»."
    )
    parent_comment_id: Optional[str] = Field(
        None, description="Идентификатор родительского комментария."
    )


class ReviewCommentCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания комментария к отзыву.

    Attributes:
        comment_id: Идентификатор комментария
    """
    comment_id: Optional[str] = Field(
        None, description="Идентификатор комментария."
    )
