from typing import Optional

from pydantic import Field, BaseModel


class PostingFBSFilterWith(BaseModel):
    """Дополнительные поля, которые нужно добавить в ответ.

    Attributes:
        analytics_data: Добавить в ответ данные аналитики (опционально)
        barcodes: Добавить в ответ штрихкоды отправления (опционально)
        financial_data: Добавить в ответ финансовые данные (опционально)
        legal_info: Добавить в ответ юридическую информацию (опционально)
        translit: Выполнить транслитерацию возвращаемых значений (опционально)
    """
    analytics_data: Optional[bool] = Field(
        False, description="Добавить в ответ данные аналитики."
    )
    barcodes: Optional[bool] = Field(
        False, description="Добавить в ответ штрихкоды отправления."
    )
    financial_data: Optional[bool] = Field(
        False, description="Добавить в ответ финансовые данные."
    )
    legal_info: Optional[bool] = Field(
        False, description="Добавить в ответ юридическую информацию."
    )
    translit: Optional[bool] = Field(
        False, description="Выполнить транслитерацию возвращаемых значений."
    )