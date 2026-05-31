import pytest

from src.ozonapi.seller.schemas.reports import ReportInfoRequest, ReportInfoResponse


class TestReportInfo:
    """Тесты для метода report_info."""

    @pytest.mark.asyncio
    async def test_report_info(self, api, mock_api_request):
        """Тестирует метод report_info."""

        mock_api_request.return_value = {
            "result": {"code": "rc-1", "status": "success", "report_type": "SELLER_PRODUCTS", "file": "http://f"}
        }

        request = ReportInfoRequest(code="rc-1")

        response = await api.report_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportInfoResponse)
        assert response.result.status == "success"
        assert response.result.file == "http://f"
