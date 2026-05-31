from ...core import APIManager
from ...schemas.rating import RatingSummaryResponse


class RatingSummaryMixin(APIManager):
    """Реализует метод /v1/rating/summary"""

    async def rating_summary(
            self: "RatingSummaryMixin"
    ) -> RatingSummaryResponse:
        """Возвращает информацию о текущих рейтингах продавца.

        Notes:
            • Рейтинги сгруппированы; по каждому доступны текущее и предыдущее значение,
              направление изменения и пороговые статусы. Также возвращает индекс
              локализации и признаки подписок Premium/Premium Plus.

        References:
            https://docs.ozon.ru/api/seller/#operation/RatingAPI_RatingSummaryV1

        Returns:
            Информация о текущих рейтингах по схеме `RatingSummaryResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.rating_summary()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="rating/summary",
            payload={},
        )
        return RatingSummaryResponse(**response)
