from ...core import APIManager
from ...schemas.analytics import (
    AnalyticsProductQueriesRequest,
    AnalyticsProductQueriesResponse,
)


class AnalyticsProductQueriesMixin(APIManager):
    """Реализует метод /v1/analytics/product-queries"""

    async def analytics_product_queries(
            self: "AnalyticsProductQueriesMixin",
            request: AnalyticsProductQueriesRequest,
    ) -> AnalyticsProductQueriesResponse:
        """Получает информацию о поисковых запросах по товарам продавца (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Возвращает по каждому товару метрики: оборот, позицию, уникальных
              пользователей поиска и просмотра, конверсию в просмотр.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueries

        Args:
            request: Параметры запроса по схеме `AnalyticsProductQueriesRequest`

        Returns:
            Информация о запросах товаров по схеме `AnalyticsProductQueriesResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_product_queries(
                    AnalyticsProductQueriesRequest(
                        date_from="2026-05-01T00:00:00Z",
                        date_to="2026-05-31T23:59:59Z",
                        page=1, page_size=50,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/product-queries",
            payload=request.model_dump(),
        )
        return AnalyticsProductQueriesResponse(**response)
