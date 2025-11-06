from typing import Any

from pydantic import BaseModel, Field


class ResponseCursor(BaseModel):
    """Базовый класс, описывающий схему ответа с курсором."""
    cursor: str = Field(
        ..., description="Указатель для выборки следующего чанка данных."
    )
    total: int = Field(
        ..., description="Общее количество результатов."
    )


class ResponseHasNext(BaseModel):
    """Базовая схема ответа, содержащего атрибут has_next."""
    has_next: bool = Field(
        ..., description="Признак, что в ответе вернулась только часть значений."
    )
    result: list[Any] = Field(
        ..., description="Список результатов."
    )


class ResponseLastId(BaseModel):
    """Базовая схема ответа, содержащего атрибут last_id."""
    last_id: str = Field(
        ..., description="Идентификатор последнего значения на странице."
    )
    total: int = Field(
        ..., description="Общее количество товаров в выборке."
    )
