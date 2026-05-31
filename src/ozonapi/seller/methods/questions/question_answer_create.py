from ...core import APIManager
from ...schemas.questions import (
    QuestionAnswerCreateRequest,
    QuestionAnswerCreateResponse,
)


class QuestionAnswerCreateMixin(APIManager):
    """Реализует метод /v1/question/answer/create"""

    async def question_answer_create(
            self: "QuestionAnswerCreateMixin",
            request: QuestionAnswerCreateRequest
    ) -> QuestionAnswerCreateResponse:
        """Метод для создания ответа на вопрос.

        Notes:
            • Публикует ответ продавца на вопрос покупателя (текст от 2 до 3000 символов).
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_AnswerCreate

        Args:
            request: Запрос на создание ответа по схеме `QuestionAnswerCreateRequest`

        Returns:
            Идентификатор ответа по схеме `QuestionAnswerCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_answer_create(
                    QuestionAnswerCreateRequest(
                        question_id="q-1",
                        sku=987654,
                        text="Да, товар совместим."
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/answer/create",
            payload=request.model_dump()
        )
        return QuestionAnswerCreateResponse(**response)
