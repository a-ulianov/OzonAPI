"""Базовые (переиспользуемые) модели раздела «Отмены заказов»."""
from typing import Optional

from pydantic import BaseModel, Field


class CancelReason(BaseModel):
    """Причина отмены заказа или отправления.

    Attributes:
        id: Идентификатор причины отмены
        name: Название причины отмены
    """

    id: Optional[int] = Field(
        None, description="Идентификатор причины отмены."
    )
    name: Optional[str] = Field(
        None, description="Название причины отмены."
    )
