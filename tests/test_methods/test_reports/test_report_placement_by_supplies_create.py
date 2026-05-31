import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportPlacementBySuppliesCreateRequest,
    ReportPlacementBySuppliesCreateResponse,
)


class TestReportPlacementBySuppliesCreate:
    """Тесты для метода report_placement_by_supplies_create."""

    @pytest.mark.asyncio
    async def test_report_placement_by_supplies_create(self, api, mock_api_request):
        """Тестирует метод report_placement_by_supplies_create."""

        mock_api_request.return_value = {"code": "rc-7"}

        request = ReportPlacementBySuppliesCreateRequest(date_from="2026-01-01", date_to="2026-02-01")

        response = await api.report_placement_by_supplies_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/placement/by-supplies/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportPlacementBySuppliesCreateResponse)
        assert response.code == "rc-7"
