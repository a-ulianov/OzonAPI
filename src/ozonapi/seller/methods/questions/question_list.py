from ...core import APIManager
from ...schemas.questions import QuestionListRequest, QuestionListResponse


class QuestionListMixin(APIManager):
    """Реализует метод /v1/question/list"""

    async def question_list(
            self: "QuestionListMixin",
            request: QuestionListRequest
    ) -> QuestionListResponse:
        """Метод для получения списка вопросов.

        Notes:
            • Возвращает вопросы покупателей с фильтрацией по статусу и дате.
            • Постраничный вывод через `limit` и `last_id`.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_List

        Args:
            request: Запрос на получение списка вопросов по схеме `QuestionListRequest`

        Returns:
            Список вопросов по схеме `QuestionListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_list(
                    QuestionListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/list",
            payload=request.model_dump()
        )
        return QuestionListResponse(**response)
