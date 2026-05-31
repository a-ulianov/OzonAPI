import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportWarehouseStockRequest,
    ReportWarehouseStockResponse,
)


class TestReportWarehouseStock:
    """Тесты для метода report_warehouse_stock."""

    @pytest.mark.asyncio
    async def test_report_warehouse_stock(self, api, mock_api_request):
        """Тестирует метод report_warehouse_stock."""

        mock_api_request.return_value = {"result": {"code": "rc-5"}}

        request = ReportWarehouseStockRequest(warehouseId=["12345"])

        response = await api.report_warehouse_stock(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/warehouse/stock",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportWarehouseStockResponse)
        assert response.result.code == "rc-5"
