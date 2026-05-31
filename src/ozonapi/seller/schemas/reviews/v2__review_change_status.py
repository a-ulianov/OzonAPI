"""https://docs.ozon.ru/api/seller/#operation/Review_ChangeStatusV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewChangeStatusRequest(BaseModel):
    """Описывает схему запроса на изменение статуса отзывов.

    Attributes:
        review_ids: Список идентификаторов отзывов
        status: Статус отзыва (`PROCESSED`, `UNPROCESSED`)
    """
    review_ids: Optional[list[str]] = Field(
        None, description="Список идентификаторов отзывов."
    )
    status: Optional[str] = Field(
        None, description="Статус отзыва: `PROCESSED` — обработан, `UNPROCESSED` — не обработан."
    )


class ReviewChangeStatusResponse(BaseModel):
    """Описывает схему ответа на запрос изменения статуса отзывов.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
