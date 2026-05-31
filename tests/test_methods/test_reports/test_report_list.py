import pytest

from src.ozonapi.seller.schemas.reports import ReportListRequest, ReportListResponse


class TestReportList:
    """Тесты для метода report_list."""

    @pytest.mark.asyncio
    async def test_report_list(self, api, mock_api_request):
        """Тестирует метод report_list."""

        mock_api_request.return_value = {
            "result": {"total": 1, "reports": [{"code": "rc-1", "status": "success"}]}
        }

        request = ReportListRequest(page=1, page_size=100)

        response = await api.report_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportListResponse)
        assert response.result.total == 1
        assert response.result.reports[0].code == "rc-1"
