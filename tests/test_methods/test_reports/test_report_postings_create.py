import pytest

from src.ozonapi.seller.schemas.reports import (
    ReportPostingsCreateRequest,
    ReportPostingsCreateResponse,
)
from src.ozonapi.seller.schemas.reports.v1__report_postings_create import (
    ReportPostingsCreateFilter,
)


class TestReportPostingsCreate:
    """Тесты для метода report_postings_create."""

    @pytest.mark.asyncio
    async def test_report_postings_create(self, api, mock_api_request):
        """Тестирует метод report_postings_create."""

        mock_api_request.return_value = {"result": {"code": "rc-3"}}

        request = ReportPostingsCreateRequest(
            filter=ReportPostingsCreateFilter(delivery_schema=["FBS"])
        )

        response = await api.report_postings_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="report/postings/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ReportPostingsCreateResponse)
        assert response.result.code == "rc-3"
