"""https://docs.ozon.ru/api/seller/#operation/Review_ChangeStatus"""
from pydantic import BaseModel, Field


class ReviewChangeStatusV1Request(BaseModel):
    """Описывает схему запроса на изменение статуса отзывов (v1).

    Attributes:
        review_ids: Массив с идентификаторами отзывов
        status: Статус отзыва (`PROCESSED`, `UNPROCESSED`)
    """
    review_ids: list[str] = Field(
        ..., description="Массив с идентификаторами отзывов."
    )
    status: str = Field(
        ..., description="Статус отзыва: `PROCESSED` — обработан, `UNPROCESSED` — не обработан."
    )


class ReviewChangeStatusV1Response(BaseModel):
    """Описывает схему ответа на запрос изменения статуса отзывов (v1).

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
