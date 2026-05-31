from ...core import APIManager
from ...schemas.reviews import ReviewCountV1Response


class ReviewCountV1Mixin(APIManager):
    """Реализует метод /v1/review/count"""

    async def review_count_v1(
            self: "ReviewCountV1Mixin"
    ) -> ReviewCountV1Response:
        """Метод для получения количества отзывов по статусам (v1).

        Notes:
            • Устаревшая версия; для новых интеграций используйте `review_count()` (v2).
            • Метод не принимает параметров.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_Count

        Returns:
            Количество отзывов по статусам по схеме `ReviewCountV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_count_v1()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/count",
            payload={}
        )
        return ReviewCountV1Response(**response)
