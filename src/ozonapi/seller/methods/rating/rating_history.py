from ...core import APIManager
from ...schemas.rating import (
    RatingHistoryRequest,
    RatingHistoryResponse,
)


class RatingHistoryMixin(APIManager):
    """Реализует метод /v1/rating/history"""

    async def rating_history(
            self: "RatingHistoryMixin",
            request: RatingHistoryRequest
    ) -> RatingHistoryResponse:
        """Возвращает информацию о рейтингах продавца за период.

        Notes:
            • Фильтр по системным названиям рейтингов (`ratings`) и периоду.
            • При `with_premium_scores=True` ответ дополняется штрафными баллами Premium.

        References:
            https://docs.ozon.ru/api/seller/#operation/RatingAPI_RatingHistoryV1

        Args:
            request: Запрос рейтингов за период по схеме `RatingHistoryRequest`

        Returns:
            Рейтинги продавца за период по схеме `RatingHistoryResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.rating_history(
                    RatingHistoryRequest(
                        date_from="2026-04-01T00:00:00Z",
                        date_to="2026-04-30T23:59:59Z",
                        ratings=["rating_on_time"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="rating/history",
            payload=request.model_dump(by_alias=True)
        )
        return RatingHistoryResponse(**response)
