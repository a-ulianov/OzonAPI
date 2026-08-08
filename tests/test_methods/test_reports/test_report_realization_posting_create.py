import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportRealizationPostingCreateRequest,
    ReportRealizationPostingCreateResponse,
)


class TestReportRealizationPostingCreate:
    """Тесты для метода report_realization_posting_create."""

    @pytest.mark.asyncio
    async def test_report_realization_posting_create(self, api, mock_api_request):
        """Тестирует метод report_realization_posting_create."""

        mock_api_request.return_value = {"code": "rrp-7"}

        response = await api.report_realization_posting_create(
            ReportRealizationPostingCreateRequest(month=5, year=2026)
        )

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/realization/posting/create",
            payload={"month": 5, "year": 2026}
        )

        assert isinstance(response, ReportRealizationPostingCreateResponse)
        assert response.code == "rrp-7"
