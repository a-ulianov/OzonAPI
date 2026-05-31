from ...core import APIManager
from ...schemas.questions import QuestionTopSkuRequest, QuestionTopSkuResponse


class QuestionTopSkuMixin(APIManager):
    """Реализует метод /v1/question/top-sku"""

    async def question_top_sku(
            self: "QuestionTopSkuMixin",
            request: QuestionTopSkuRequest
    ) -> QuestionTopSkuResponse:
        """Метод для получения товаров с наибольшим количеством вопросов.

        Notes:
            • Возвращает список SKU товаров с наибольшим количеством вопросов.
            • Доступен продавцам с подпиской Premium Plus (раздел Вопросы-ответы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Question_TopSku

        Args:
            request: Запрос на получение топа товаров по схеме `QuestionTopSkuRequest`

        Returns:
            Список SKU товаров по схеме `QuestionTopSkuResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.question_top_sku(
                    QuestionTopSkuRequest(
                        limit=10
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="question/top-sku",
            payload=request.model_dump()
        )
        return QuestionTopSkuResponse(**response)
