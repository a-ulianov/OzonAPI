"""https://docs.ozon.ru/api/seller/#operation/Review_CommentDelete"""
from pydantic import BaseModel, Field


class ReviewCommentDeleteV1Request(BaseModel):
    """Описывает схему запроса на удаление комментария к отзыву (v1).

    Attributes:
        comment_id: Идентификатор комментария
    """
    comment_id: str = Field(
        ..., description="Идентификатор комментария."
    )


class ReviewCommentDeleteV1Response(BaseModel):
    """Описывает схему ответа на запрос удаления комментария к отзыву (v1).

    Notes:
        • При успешном удалении API возвращает пустой объект.
    """
    pass
