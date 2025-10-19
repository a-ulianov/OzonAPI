from typing import Optional, Any

from pydantic import BaseModel, Field


class PostingFBSOptional(BaseModel):
    """Список товаров с дополнительными характеристиками.

    Attributes:
        products_with_possible_mandatory_mark: Список товаров с возможной маркировкой
    """
    products_with_possible_mandatory_mark: Optional[list[Any]] = Field(
        default_factory=list, description="Список товаров с возможной маркировкой."
    )