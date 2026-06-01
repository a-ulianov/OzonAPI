import pytest

from src.ozonapi.seller.schemas.beta import (
    RemovalFromStockListRequest,
    RemovalFromStockListResponse,
)


class TestRemovalFromStockList:
    """Тесты для метода removal_from_stock_list."""

    @pytest.mark.asyncio
    async def test_removal_from_stock_list(self, api, mock_api_request):
        """Тестирует метод removal_from_stock_list."""

        mock_api_request.return_value = {
            "last_id": "xyz",
            "returns_summary_report_rows": [
                {"return_id": 9, "sku": 333, "offer_id": "art-2", "stock_type": "DEFECT"}
            ],
        }

        request = RemovalFromStockListRequest(
            date_from="2026-05-01", date_to="2026-06-01", limit=50
        )

        response = await api.removal_from_stock_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="removal/from-stock/list",
            payload=request.model_dump()
        )

        assert isinstance(response, RemovalFromStockListResponse)
        assert response.returns_summary_report_rows[0].sku == 333
