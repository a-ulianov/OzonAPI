from ...core import APIManager
from ...schemas.questions import (
    QuestionAnswerDeleteRequest,
    QuestionAnswerDeleteResponse,
)


class QuestionAnswerDeleteMixin(APIManager):
    """Реализует метод /v1/question/answer/delete"""

    async def question_answer_delete(
            self: "QuestionAnswerDeleteMixin",
            request: QuestionAnswerDeleteRequest
    ) -> QuestionAnswerDeleteResponse:
        """Метод для удаления ответа на вопрос.

        Notes:
            • Удаляет ответ продавца по идентификатору ответа и SKU товара.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_AnswerDelete

        Args:
            request: Запрос на удаление ответа по схеме `QuestionAnswerDeleteRequest`

        Returns:
            Результат удаления ответа по схеме `QuestionAnswerDeleteResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_answer_delete(
                    QuestionAnswerDeleteRequest(
                        answer_id="a-1",
                        sku=987654
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/answer/delete",
            payload=request.model_dump()
        )
        return QuestionAnswerDeleteResponse(**response)
