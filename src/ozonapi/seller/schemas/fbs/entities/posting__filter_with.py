from typing import Optional

from pydantic import Field, BaseModel

from ...entities.postings import PostingFilterWith


class PostingFBSFilterWith(PostingFilterWith):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        analytics_data: Добавить в ответ данные аналитики (опционально)
        barcodes: Добавить в ответ штрихкоды отправления (опционально)
        financial_data: Добавить в ответ финансовые данные (опционально)
        legal_info: Добавить в ответ юридическую информацию (опционально)
        translit: Выполнить транслитерацию возвращаемых значений (опционально)
    """
    barcodes: Optional[bool] = Field(
        False, description="Добавить в ответ штрихкоды отправления."
    )
    translit: Optional[bool] = Field(
        False, description="Выполнить транслитерацию возвращаемых значений."
    )