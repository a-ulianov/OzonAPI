from ...core import APIManager
from ...schemas.reviews import ReviewInfoRequest, ReviewInfoResponse


class ReviewInfoMixin(APIManager):
    """Реализует метод /v2/review/info"""

    async def review_info(
            self: "ReviewInfoMixin",
            request: ReviewInfoRequest
    ) -> ReviewInfoResponse:
        """Метод для получения информации об отзыве (v2).

        Notes:
            • Возвращает подробную информацию об отзыве: текст, оценку, статус, изображения и видео.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_InfoV2

        Args:
            request: Запрос на получение информации об отзыве по схеме `ReviewInfoRequest`

        Returns:
            Информация об отзыве по схеме `ReviewInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_info(
                    ReviewInfoRequest(
                        review_id="abc"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="review/info",
            payload=request.model_dump()
        )
        return ReviewInfoResponse(**response)
