from ...core import APIManager
from ...schemas.reviews import (
    ReviewChangeStatusV1Request,
    ReviewChangeStatusV1Response,
)


class ReviewChangeStatusV1Mixin(APIManager):
    """Реализует метод /v1/review/change-status"""

    async def review_change_status_v1(
            self: "ReviewChangeStatusV1Mixin",
            request: ReviewChangeStatusV1Request
    ) -> ReviewChangeStatusV1Response:
        """Метод для изменения статуса отзывов (v1).

        Notes:
            • Устаревшая версия; для новых интеграций используйте `review_change_status()` (v2).
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_ChangeStatus

        Args:
            request: Запрос на изменение статуса по схеме `ReviewChangeStatusV1Request`

        Returns:
            Результат изменения статуса по схеме `ReviewChangeStatusV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_change_status_v1(
                    ReviewChangeStatusV1Request(
                        review_ids=["abc"],
                        status="PROCESSED"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/change-status",
            payload=request.model_dump()
        )
        return ReviewChangeStatusV1Response(**response)
