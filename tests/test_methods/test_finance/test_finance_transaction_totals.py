import pytest

from src.ozonapi.seller.schemas.finance import (
    FinancePeriod,
    FinanceTransactionTotalsRequest,
    FinanceTransactionTotalsResponse,
)


class TestFinanceTransactionTotals:
    """Тесты для метода finance_transaction_totals."""

    @pytest.mark.asyncio
    async def test_finance_transaction_totals(self, api, mock_api_request):
        """Тестирует метод finance_transaction_totals."""

        mock_api_request.return_value = {
            "result": {
                "accruals_for_sale": 10000.0,
                "sale_commission": -1500.0,
                "processing_and_delivery": -300.0,
                "compensation_amount": 0.0,
            }
        }

        request = FinanceTransactionTotalsRequest(
            date=FinancePeriod(
                from_="2026-04-01T00:00:00.000Z", to="2026-04-30T23:59:59.999Z"
            )
        )

        response = await api.finance_transaction_totals(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="finance/transaction/totals",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceTransactionTotalsResponse)
        assert response.result.accruals_for_sale == 10000.0
        assert response.result.sale_commission == -1500.0
