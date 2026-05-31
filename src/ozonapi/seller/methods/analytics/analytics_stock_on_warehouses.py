from ...core import APIManager
from ...schemas.analytics import (
    AnalyticsStockOnWarehousesRequest,
    AnalyticsStockOnWarehousesResponse,
)


class AnalyticsStockOnWarehousesMixin(APIManager):
    """Реализует метод /v2/analytics/stock_on_warehouses"""

    async def analytics_stock_on_warehouses(
            self: "AnalyticsStockOnWarehousesMixin",
            request: AnalyticsStockOnWarehousesRequest
    ) -> AnalyticsStockOnWarehousesResponse:
        """Возвращает отчёт по остаткам и товарам в перемещении по складам.

        Notes:
            • Постраничная выдача через `limit`/`offset`; можно отфильтровать по типу склада.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsGetStockOnWarehousesV2

        Args:
            request: Запрос отчёта по схеме `AnalyticsStockOnWarehousesRequest`

        Returns:
            Отчёт по остаткам по схеме `AnalyticsStockOnWarehousesResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_stock_on_warehouses(
                    AnalyticsStockOnWarehousesRequest(limit=100, offset=0)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="analytics/stock_on_warehouses",
            payload=request.model_dump(by_alias=True)
        )
        return AnalyticsStockOnWarehousesResponse(**response)
