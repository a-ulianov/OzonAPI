from ...core import APIManager
from ...schemas.rating import RatingIndexFBSInfoResponse


class RatingIndexFBSInfoMixin(APIManager):
    """Реализует метод /v1/rating/index/fbs/info"""

    async def rating_index_fbs_info(
            self: "RatingIndexFBSInfoMixin"
    ) -> RatingIndexFBSInfoResponse:
        """Возвращает индекс ошибок FBS и rFBS за расчётный период.

        Notes:
            • Содержит итоговый индекс ошибок, расходы на обработку ошибок и
              динамику индекса по дням за расчётный период.

        References:
            https://docs.ozon.ru/api/seller/#operation/RatingAPI_GetFBSRatingIndexInfoV1

        Returns:
            Индекс ошибок FBS и rFBS по схеме `RatingIndexFBSInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.rating_index_fbs_info()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="rating/index/fbs/info",
            payload={},
        )
        return RatingIndexFBSInfoResponse(**response)
