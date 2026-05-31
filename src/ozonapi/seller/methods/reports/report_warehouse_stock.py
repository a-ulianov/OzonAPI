from ...core import APIManager
from ...schemas.reports import (
    ReportWarehouseStockRequest,
    ReportWarehouseStockResponse,
)


class ReportWarehouseStockMixin(APIManager):
    """Реализует метод /v1/report/warehouse/stock"""

    async def report_warehouse_stock(
            self: "ReportWarehouseStockMixin",
            request: ReportWarehouseStockRequest
    ) -> ReportWarehouseStockResponse:
        """Метод для создания отчёта об остатках на FBS-складе.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateWarehouseStockReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportWarehouseStockRequest`

        Returns:
            Код отчёта по схеме `ReportWarehouseStockResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_warehouse_stock(
                    ReportWarehouseStockRequest(
                        warehouseId=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/warehouse/stock",
            payload=request.model_dump()
        )
        return ReportWarehouseStockResponse(**response)
