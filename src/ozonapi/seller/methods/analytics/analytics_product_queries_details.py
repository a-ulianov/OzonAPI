from ...core import APIManager
from ...schemas.analytics import (
    AnalyticsProductQueriesDetailsRequest,
    AnalyticsProductQueriesDetailsResponse,
)


class AnalyticsProductQueriesDetailsMixin(APIManager):
    """Реализует метод /v1/analytics/product-queries/details"""

    async def analytics_product_queries_details(
            self: "AnalyticsProductQueriesDetailsMixin",
            request: AnalyticsProductQueriesDetailsRequest,
    ) -> AnalyticsProductQueriesDetailsResponse:
        """Получает детализацию поисковых запросов по товару (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Возвращает по каждому товару отдельные поисковые запросы с метриками.
            • `limit_by_sku` ограничивает число запросов на один SKU.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueriesDetails

        Args:
            request: Параметры запроса по схеме `AnalyticsProductQueriesDetailsRequest`

        Returns:
            Детализация запросов по товару по схеме
            `AnalyticsProductQueriesDetailsResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_product_queries_details(
                    AnalyticsProductQueriesDetailsRequest(
                        date_from="2026-05-01T00:00:00Z",
                        date_to="2026-05-31T23:59:59Z",
                        skus=["1234567890"],
                        limit_by_sku=10,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/product-queries/details",
            payload=request.model_dump(),
        )
        return AnalyticsProductQueriesDetailsResponse(**response)
