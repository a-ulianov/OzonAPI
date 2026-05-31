import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportPlacementByProductsCreateRequest,
    ReportPlacementByProductsCreateResponse,
)


class TestReportPlacementByProductsCreate:
    """Тесты для метода report_placement_by_products_create."""

    @pytest.mark.asyncio
    async def test_report_placement_by_products_create(self, api, mock_api_request):
        """Тестирует метод report_placement_by_products_create."""

        mock_api_request.return_value = {"code": "rc-6"}

        request = ReportPlacementByProductsCreateRequest(date_from="2026-01-01", date_to="2026-02-01")

        response = await api.report_placement_by_products_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/placement/by-products/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportPlacementByProductsCreateResponse)
        assert response.code == "rc-6"
