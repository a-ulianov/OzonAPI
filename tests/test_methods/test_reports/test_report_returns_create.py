import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportReturnsCreateRequest,
    ReportReturnsCreateResponse,
)
from src.ozonapi.seller.schemas.reports.v2__report_returns_create import (
    ReportReturnsCreateFilter,
)


class TestReportReturnsCreate:
    """Тесты для метода report_returns_create."""

    @pytest.mark.asyncio
    async def test_report_returns_create(self, api, mock_api_request):
        """Тестирует метод report_returns_create."""

        mock_api_request.return_value = {"result": {"code": "rc-2"}}

        request = ReportReturnsCreateRequest(
            filter=ReportReturnsCreateFilter(delivery_schema="FBS")
        )

        response = await api.report_returns_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="report/returns/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportReturnsCreateResponse)
        assert response.result.code == "rc-2"
