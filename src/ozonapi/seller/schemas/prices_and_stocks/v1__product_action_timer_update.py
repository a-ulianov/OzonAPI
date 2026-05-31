"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductActionTimerUpdate"""
from pydantic import BaseModel, Field


class ProductActionTimerUpdateRequest(BaseModel):
    """Схема запроса на обновление таймера актуальности минимальной цены.

    Attributes:
        product_ids: Список идентификаторов товаров в системе Ozon — product_id (максимум 1000)
    """
    product_ids: list[str] = Field(
        ..., description="Список идентификаторов товаров в системе Ozon — product_id.",
        min_length=1, max_length=1000
    )


class ProductActionTimerUpdateResponse(BaseModel):
    """Схема ответа на запрос обновления таймера актуальности минимальной цены.

    Notes:
        • Метод возвращает пустое тело ответа при успешном обновлении таймера.
    """
    pass
