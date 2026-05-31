"""Композиция миксинов методов раздела Вопросы и ответы (beta).

Объединяет методы работы с вопросами покупателей и ответами на них
в единый класс :class:`SellerQuestionAPI`.
"""

from ...core import APIManager
from .question_answer_create import QuestionAnswerCreateMixin
from .question_answer_delete import QuestionAnswerDeleteMixin
from .question_answer_list import QuestionAnswerListMixin
from .question_change_status import QuestionChangeStatusMixin
from .question_count import QuestionCountMixin
from .question_info import QuestionInfoMixin
from .question_list import QuestionListMixin
from .question_top_sku import QuestionTopSkuMixin


class SellerQuestionAPI(
    QuestionAnswerCreateMixin,
    QuestionAnswerDeleteMixin,
    QuestionAnswerListMixin,
    QuestionChangeStatusMixin,
    QuestionCountMixin,
    QuestionInfoMixin,
    QuestionListMixin,
    QuestionTopSkuMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Вопросы и ответы (beta).

    Notes:
        • Объединяет методы получения списка/информации/количества вопросов,
          управления статусом вопросов и работы с ответами на них.
        • Раздел доступен продавцам с подпиской Premium Plus.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Question
    """

    pass
