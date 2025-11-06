from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.products import Visibility
from ..entities.common import RequestLimit1000, RequestCursor


class BaseRequestFilterSpec(BaseModel):
    """Базовый класс фильтра запроса."""
    offer_id: Optional[list[str]] = Field(
        default_factory=list, description="Фильтр по параметру offer_id. Можно передавать до 1000 значений.",
        max_length=1000,
    )
    product_id: Optional[list[int]] = Field(
        default_factory=list, description="Фильтр по параметру product_id. Можно передавать до 1000 значений.",
        max_length=1000,
    )
    visibility: Optional[Visibility] = Field(
        Visibility.ALL, description="Фильтр по видимости товара."
    )


class BaseRequestCursorSpec(RequestLimit1000, RequestCursor):
    """Базовый класс запроса с курсором."""
    pass