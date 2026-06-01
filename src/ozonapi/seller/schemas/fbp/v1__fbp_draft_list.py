"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpDraftItem


class FbpDraftListRequest(BaseModel):
    """Схема запроса списка черновиков поставки FBP.

    Attributes:
        count: Количество черновиков в ответе
        last_id: Идентификатор последнего черновика предыдущей страницы (пагинация)
    """

    count: int = Field(
        ..., description="Количество черновиков в ответе."
    )
    last_id: Optional[int] = Field(
        None,
        description="Идентификатор последнего черновика предыдущей страницы "
                    "(для постраничной выборки)."
    )


class FbpDraftListResponse(BaseModel):
    """Схема ответа со списком черновиков поставки FBP.

    Attributes:
        items: Список черновиков поставки
        has_next: Признак наличия следующей страницы
    """

    items: list[FbpDraftItem] = Field(
        default_factory=list, description="Список черновиков поставки."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
