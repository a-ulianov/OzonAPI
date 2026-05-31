"""https://docs.ozon.ru/api/seller/#operation/Review_CommentDeleteV2"""
from pydantic import BaseModel, Field


class ReviewCommentDeleteRequest(BaseModel):
    """Описывает схему запроса на удаление комментария к отзыву.

    Attributes:
        comment_id: Идентификатор комментария
        sku: Идентификатор товара в системе Ozon — SKU
    """
    comment_id: str = Field(
        ..., description="Идентификатор комментария."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class ReviewCommentDeleteResponse(BaseModel):
    """Описывает схему ответа на запрос удаления комментария к отзыву.

    Notes:
        • При успешном удалении API возвращает пустой объект.
    """
    pass
