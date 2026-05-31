"""Общая модель вопроса покупателя."""
from typing import Optional

from pydantic import BaseModel, Field


class Question(BaseModel):
    """Вопрос покупателя.

    Attributes:
        id: Идентификатор вопроса
        sku: Идентификатор товара в системе Ozon — SKU
        text: Текст вопроса
        author_name: Имя автора вопроса
        published_at: Дата публикации вопроса
        question_link: Ссылка на вопрос
        product_url: Ссылка на товар
        answers_count: Количество ответов на вопрос
        status: Статус вопроса (`NEW`, `VIEWED`, `PROCESSED` и т.д.)
    """
    id: Optional[str] = Field(
        None, description="Идентификатор вопроса."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    text: Optional[str] = Field(
        None, description="Текст вопроса."
    )
    author_name: Optional[str] = Field(
        None, description="Имя автора вопроса."
    )
    published_at: Optional[str] = Field(
        None, description="Дата публикации вопроса."
    )
    question_link: Optional[str] = Field(
        None, description="Ссылка на вопрос."
    )
    product_url: Optional[str] = Field(
        None, description="Ссылка на товар."
    )
    answers_count: Optional[int] = Field(
        None, description="Количество ответов на вопрос."
    )
    status: Optional[str] = Field(
        None, description="Статус вопроса: `NEW` — новый, `VIEWED` — просмотренный, `PROCESSED` — обработанный."
    )
