from ...core import APIManager
from ...schemas.reviews import ReviewInfoV1Request, ReviewInfoV1Response


class ReviewInfoV1Mixin(APIManager):
    """Реализует метод /v1/review/info"""

    async def review_info_v1(
            self: "ReviewInfoV1Mixin",
            request: ReviewInfoV1Request
    ) -> ReviewInfoV1Response:
        """Метод для получения информации об отзыве (v1).

        Notes:
            • Устаревшая версия; для новых интеграций используйте `review_info()` (v2).
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_Info

        Args:
            request: Запрос на получение информации об отзыве по схеме `ReviewInfoV1Request`

        Returns:
            Информация об отзыве по схеме `ReviewInfoV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_info_v1(
                    ReviewInfoV1Request(
                        review_id="abc"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/info",
            payload=request.model_dump()
        )
        return ReviewInfoV1Response(**response)
