from ...core import APIManager
from ...schemas.questions import QuestionAnswerListRequest, QuestionAnswerListResponse


class QuestionAnswerListMixin(APIManager):
    """Реализует метод /v1/question/answer/list"""

    async def question_answer_list(
            self: "QuestionAnswerListMixin",
            request: QuestionAnswerListRequest
    ) -> QuestionAnswerListResponse:
        """Метод для получения списка ответов на вопрос.

        Notes:
            • Возвращает ответы на указанный вопрос со статусом публикации.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_AnswerList

        Args:
            request: Запрос на получение списка ответов по схеме `QuestionAnswerListRequest`

        Returns:
            Список ответов по схеме `QuestionAnswerListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_answer_list(
                    QuestionAnswerListRequest(
                        question_id="q-1",
                        sku=987654
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/answer/list",
            payload=request.model_dump()
        )
        return QuestionAnswerListResponse(**response)
