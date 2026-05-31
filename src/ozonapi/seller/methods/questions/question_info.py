from ...core import APIManager
from ...schemas.questions import QuestionInfoRequest, QuestionInfoResponse


class QuestionInfoMixin(APIManager):
    """Реализует метод /v1/question/info"""

    async def question_info(
            self: "QuestionInfoMixin",
            request: QuestionInfoRequest
    ) -> QuestionInfoResponse:
        """Метод для получения информации о вопросе.

        Notes:
            • Возвращает информацию о вопросе: текст, автора, статус, ссылки и количество ответов.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_Info

        Args:
            request: Запрос на получение информации о вопросе по схеме `QuestionInfoRequest`

        Returns:
            Информация о вопросе по схеме `QuestionInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_info(
                    QuestionInfoRequest(
                        question_id="q-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/info",
            payload=request.model_dump()
        )
        return QuestionInfoResponse(**response)
