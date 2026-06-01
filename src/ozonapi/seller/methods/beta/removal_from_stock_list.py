from ...core import APIManager
from ...schemas.beta import (
    RemovalFromStockListRequest,
    RemovalFromStockListResponse,
)


class RemovalFromStockListMixin(APIManager):
    """Реализует метод /v1/removal/from-stock/list"""

    async def removal_from_stock_list(
            self: "RemovalFromStockListMixin",
            request: RemovalFromStockListRequest
    ) -> RemovalFromStockListResponse:
        """Возвращает отчёт по вывозу и утилизации товаров со стока FBO.

        Notes:
            • Пагинация по `last_id`: передайте полученный `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetSupplierReturnsSummaryReport

        Args:
            request: Запрос по схеме `RemovalFromStockListRequest`

        Returns:
            Отчёт по схеме `RemovalFromStockListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.removal_from_stock_list(
                    RemovalFromStockListRequest(date_from="2026-05-01", date_to="2026-06-01", limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="removal/from-stock/list",
            payload=request.model_dump()
        )
        return RemovalFromStockListResponse(**response)
