from ...core import APIManager
from ...schemas.reviews import ReviewCountResponse


class ReviewCountMixin(APIManager):
    """Реализует метод /v2/review/count"""

    async def review_count(
            self: "ReviewCountMixin"
    ) -> ReviewCountResponse:
        """Метод для получения количества отзывов по статусам (v2).

        Notes:
            • Возвращает количество отзывов в разрезе статусов (всего, новые, просмотренные, обработанные).
            • Метод не принимает параметров.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_CountV2

        Returns:
            Количество отзывов по статусам по схеме `ReviewCountResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_count()
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="review/count",
            payload={}
        )
        return ReviewCountResponse(**response)
