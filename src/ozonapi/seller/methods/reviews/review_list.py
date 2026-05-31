from ...core import APIManager
from ...schemas.reviews import ReviewListRequest, ReviewListResponse


class ReviewListMixin(APIManager):
    """Реализует метод /v2/review/list"""

    async def review_list(
            self: "ReviewListMixin",
            request: ReviewListRequest
    ) -> ReviewListResponse:
        """Метод для получения списка отзывов (v2).

        Notes:
            • Возвращает отзывы с фильтрацией по статусу, статусу заказа, товарам и дате.
            • Постраничный вывод через `limit` и `last_id`.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_ListV2

        Args:
            request: Запрос на получение списка отзывов по схеме `ReviewListRequest`

        Returns:
            Список отзывов по схеме `ReviewListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_list(
                    ReviewListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="review/list",
            payload=request.model_dump()
        )
        return ReviewListResponse(**response)
