from ...core import APIManager
from ...schemas.reviews import ReviewListV1Request, ReviewListV1Response


class ReviewListV1Mixin(APIManager):
    """Реализует метод /v1/review/list"""

    async def review_list_v1(
            self: "ReviewListV1Mixin",
            request: ReviewListV1Request
    ) -> ReviewListV1Response:
        """Метод для получения списка отзывов (v1).

        Notes:
            • Устаревшая версия с плоским фильтром по статусу; для новых интеграций
              используйте `review_list()` (v2).
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_List

        Args:
            request: Запрос на получение списка отзывов по схеме `ReviewListV1Request`

        Returns:
            Список отзывов по схеме `ReviewListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_list_v1(
                    ReviewListV1Request(
                        limit=100,
                        status="ALL"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/list",
            payload=request.model_dump()
        )
        return ReviewListV1Response(**response)
