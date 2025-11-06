"""https://docs.ozon.com/api/seller/?#operation/PostingAPI_GetPostingFboCancelReasonList"""
from pydantic import BaseModel, Field

from ..entities.postings import PostingCancelReasonListItem


class PostingFBOCancelReasonListResponse(BaseModel):
    """Возвращает список возможных причин отправлений.

    Attributes:
        result: список возможных причин отправлений
    """
    model_config = {'frozen': True}

    result: list[PostingCancelReasonListItem] = Field(
        ..., description="Cписок возможных причин отправлений."
    )
