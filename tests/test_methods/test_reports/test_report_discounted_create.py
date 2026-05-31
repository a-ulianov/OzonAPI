import pytest

from src.ozonapi.seller.schemas.reports import ReportDiscountedCreateResponse


class TestReportDiscountedCreate:
    """Тесты для метода report_discounted_create."""

    @pytest.mark.asyncio
    async def test_report_discounted_create(self, api, mock_api_request):
        """Тестирует метод report_discounted_create."""

        mock_api_request.return_value = {"code": "rc-4"}

        response = await api.report_discounted_create()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/discounted/create",
            payload={}
        )

        assert isinstance(response, ReportDiscountedCreateResponse)
        assert response.code == "rc-4"
