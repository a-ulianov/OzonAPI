from ...core import APIManager
from ...schemas.beta import AnalyticsStocksRequest, AnalyticsStocksResponse


class AnalyticsStocksMixin(APIManager):
    """Реализует метод /v1/analytics/stocks"""

    async def analytics_stocks(
            self: "AnalyticsStocksMixin",
            request: AnalyticsStocksRequest
    ) -> AnalyticsStocksResponse:
        """Получает аналитику по остаткам товаров на складах.

        Notes:
            • Метод соответствует разделу FBO → Управление остатками в личном кабинете.
            • Аналитика обновляется раз в день в 07:00 UTC, поэтому остатки могут не совпадать с фактическими.
            • В запросе обязательным является только список SKU `skus`, остальные поля опциональны.
            • В одном запросе можно передать до `100` SKU.
            • Получить идентификаторы складов `warehouse_ids` можно методом `warehouse_list()`
            • Получить идентификаторы кластеров `cluster_ids` можно через метод `cluster_list()`.

        References:
            https://docs.ozon.com/api/seller/?#operation/AnalyticsAPI_AnalyticsStocks

        Args:
            request: Фильтры для получения аналитики по остаткам по схеме `AnalyticsStocksRequest`.

        Returns:
            Аналитика по остаткам товаров с детализацией по складам и кластерам по схеме `AnalyticsStocksResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_stocks(
                    AnalyticsStocksRequest(
                        skus=[123456789, 987654321],
                        cluster_ids=[1, 2, 3],
                        warehouse_ids=[101, 102],
                        item_tags=[ItemTag.ECONOM, ItemTag.NOVEL],
                        turnover_grades=[TurnoverGrade.DEFICIT, TurnoverGrade.POPULAR]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/stocks",
            payload=request.model_dump(),
        )
        return AnalyticsStocksResponse(**response)