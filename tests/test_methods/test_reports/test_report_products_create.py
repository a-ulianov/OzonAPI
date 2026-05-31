import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportProductsCreateRequest,
    ReportProductsCreateResponse,
)


class TestReportProductsCreate:
    """Тесты для метода report_products_create."""

    @pytest.mark.asyncio
    async def test_report_products_create(self, api, mock_api_request):
        """Тестирует метод report_products_create."""

        mock_api_request.return_value = {"result": {"code": "rc-1"}}

        request = ReportProductsCreateRequest(language="DEFAULT")

        response = await api.report_products_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/products/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReportProductsCreateResponse)
        assert response.result.code == "rc-1"
