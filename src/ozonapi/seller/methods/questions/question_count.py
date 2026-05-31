from ...core import APIManager
from ...schemas.questions import QuestionCountResponse


class QuestionCountMixin(APIManager):
    """Реализует метод /v1/question/count"""

    async def question_count(
            self: "QuestionCountMixin"
    ) -> QuestionCountResponse:
        """Метод для получения количества вопросов по статусам.

        Notes:
            • Возвращает количество вопросов в разрезе статусов (всего, новые, просмотренные и т.д.).
            • Метод не принимает параметров.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_Count

        Returns:
            Количество вопросов по статусам по схеме `QuestionCountResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_count()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/count",
            payload={}
        )
        return QuestionCountResponse(**response)
