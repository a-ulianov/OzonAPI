from ...core import APIManager
from ...schemas.analytics import (
    AnalyticsTurnoverStocksRequest,
    AnalyticsTurnoverStocksResponse,
)


class AnalyticsTurnoverStocksMixin(APIManager):
    """Реализует метод /v1/analytics/turnover/stocks"""

    async def analytics_turnover_stocks(
            self: "AnalyticsTurnoverStocksMixin",
            request: AnalyticsTurnoverStocksRequest
    ) -> AnalyticsTurnoverStocksResponse:
        """Возвращает оборачиваемость товаров и уровень остатков.

        Notes:
            • Для каждого товара — среднесуточные продажи, остаток, дни до исчерпания
              и цветовые уровни остатка/оборачиваемости (`GRADES_*`).
            • Постраничная выдача через `limit`/`offset`; фильтр по списку SKU.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsTurnoverStocks

        Args:
            request: Запрос оборачиваемости по схеме `AnalyticsTurnoverStocksRequest`

        Returns:
            Оборачиваемость товаров по схеме `AnalyticsTurnoverStocksResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_turnover_stocks(
                    AnalyticsTurnoverStocksRequest(limit=100, offset=0)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/turnover/stocks",
            payload=request.model_dump(by_alias=True)
        )
        return AnalyticsTurnoverStocksResponse(**response)
