from ...core import APIManager
from ...schemas.reviews import ReviewChangeStatusRequest, ReviewChangeStatusResponse


class ReviewChangeStatusMixin(APIManager):
    """Реализует метод /v2/review/change-status"""

    async def review_change_status(
            self: "ReviewChangeStatusMixin",
            request: ReviewChangeStatusRequest
    ) -> ReviewChangeStatusResponse:
        """Метод для изменения статуса отзывов (v2).

        Notes:
            • Переводит указанные отзывы в статус `PROCESSED` или `UNPROCESSED`.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_ChangeStatusV2

        Args:
            request: Запрос на изменение статуса по схеме `ReviewChangeStatusRequest`

        Returns:
            Результат изменения статуса по схеме `ReviewChangeStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_change_status(
                    ReviewChangeStatusRequest(
                        review_ids=["abc"],
                        status="PROCESSED"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="review/change-status",
            payload=request.model_dump()
        )
        return ReviewChangeStatusResponse(**response)
