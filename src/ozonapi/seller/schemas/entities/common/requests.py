from typing import Optional

from pydantic import BaseModel, Field


class RequestLastId(BaseModel):
    """Базовая схема запроса с last_id."""
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего товара для пагинации."
    )
    limit: int = Field(
        ..., description="Максимальное количество возвращаемых запросом значений.",
    )


class RequestLimit1000(BaseModel):
    """Базовая схема запроса с limit<=1000."""
    limit: Optional[int] = Field(
        1000, description="Максимальное количество товаров в ответе (максимум 1000).",
        ge=1, le=1000
    )


class RequestOffset(BaseModel):
    """Базовая схема запроса с offset."""
    limit: int = Field(
        ..., description="Количество элементов в ответе.",
    )
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class RequestCursor(BaseModel):
    """Базовая схема запроса с курсором."""
    cursor: Optional[str] = Field(
        default_factory=str, description="Указатель для выборки следующего чанка данных."
    )
    limit: int = Field(
        ..., description="Максимальное количество возвращаемых запросом значений.",
    )
