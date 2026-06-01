from ...core import APIManager
from ...schemas.beta import (
    AnalyticsManageStocksRequest,
    AnalyticsManageStocksResponse,
)


class AnalyticsManageStocksMixin(APIManager):
    """Реализует метод /v1/analytics/manage/stocks"""

    async def analytics_manage_stocks(
            self: "AnalyticsManageStocksMixin",
            request: AnalyticsManageStocksRequest
    ) -> AnalyticsManageStocksResponse:
        """Возвращает остатки товаров по типам (годные, бракованные и др.) на складах.

        Notes:
            • Соответствует разделу FBO → Управление остатками в личном кабинете.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_ManageStocks

        Args:
            request: Запрос по схеме `AnalyticsManageStocksRequest`

        Returns:
            Остатки товаров по схеме `AnalyticsManageStocksResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_manage_stocks(
                    AnalyticsManageStocksRequest(limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/manage/stocks",
            payload=request.model_dump()
        )
        return AnalyticsManageStocksResponse(**response)
