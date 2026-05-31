import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportMarkedProductsSalesCreateRequest,
    ReportMarkedProductsSalesCreateResponse,
)
from src.ozonapi.seller.schemas.reports.v1__report_marked_products_sales_create import (
    ReportMarkedProductsSalesCreateDate,
)


class TestReportMarkedProductsSalesCreate:
    """Тесты для метода report_marked_products_sales_create."""

    @pytest.mark.asyncio
    async def test_report_marked_products_sales_create(self, api, mock_api_request):
        """Тестирует метод report_marked_products_sales_create."""

        mock_api_request.return_value = {"result": {"code": "rc-8"}}

        request = ReportMarkedProductsSalesCreateRequest(
            date=ReportMarkedProductsSalesCreateDate(from_="2026-01-01", to="2026-02-01")
        )

        response = await api.report_marked_products_sales_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/marked-products-sales/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ReportMarkedProductsSalesCreateResponse)
        assert response.result.code == "rc-8"
