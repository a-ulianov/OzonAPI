"""https://docs.ozon.ru/api/seller/#operation/Review_Info"""
from .v2__review_info import ReviewInfoRequest, ReviewInfoResponse


class ReviewInfoV1Request(ReviewInfoRequest):
    """Описывает схему запроса на получение информации об отзыве (v1).

    Notes:
        • Схема идентична версии v2 (`ReviewInfoRequest`).
    """
    pass


class ReviewInfoV1Response(ReviewInfoResponse):
    """Описывает схему ответа на запрос информации об отзыве (v1).

    Notes:
        • Схема идентична версии v2 (`ReviewInfoResponse`).
    """
    pass
