import pytest

from src.ozonapi.seller.schemas.reports import (
    FinanceCashFlowStatementListRequest,
    FinanceCashFlowStatementListResponse,
)
from src.ozonapi.seller.schemas.reports.v1__finance_cash_flow_statement_list import (
    FinanceCashFlowPeriod,
)


class TestFinanceCashFlowStatementList:
    """Тесты для метода finance_cash_flow_statement_list."""

    @pytest.mark.asyncio
    async def test_finance_cash_flow_statement_list(self, api, mock_api_request):
        """Тестирует метод finance_cash_flow_statement_list."""

        mock_api_request.return_value = {
            "result": {
                "page_count": 1,
                "cash_flows": [
                    {"orders_amount": 1000.0, "returns_amount": 50.0, "currency_code": "RUB",
                     "period": {"id": 7, "begin": "2026-01-01", "end": "2026-01-31"}}
                ]
            }
        }

        request = FinanceCashFlowStatementListRequest(
            date=FinanceCashFlowPeriod(from_="2026-01-01T00:00:00Z", to="2026-02-01T00:00:00Z"),
            page=1,
            page_size=100
        )

        response = await api.finance_cash_flow_statement_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/cash-flow-statement/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceCashFlowStatementListResponse)
        assert response.result.cash_flows[0].orders_amount == 1000.0
        assert response.result.cash_flows[0].period.id == 7
