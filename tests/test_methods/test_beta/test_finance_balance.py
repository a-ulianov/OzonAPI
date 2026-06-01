import pytest

from src.ozonapi.seller.schemas.beta import (
    FinanceBalanceRequest,
    FinanceBalanceResponse,
)


class TestFinanceBalance:
    """Тесты для метода finance_balance."""

    @pytest.mark.asyncio
    async def test_finance_balance(self, api, mock_api_request):
        """Тестирует метод finance_balance."""

        mock_api_request.return_value = {
            "cashflows": {
                "sales": {
                    "amount": {"currency_code": "RUB", "value": 1000.0},
                    "amount_details": {
                        "partner_programs": {"currency_code": "RUB", "value": 10.0},
                        "points_for_discounts": "5",
                        "revenue": {"currency_code": "RUB", "value": 990.0},
                    },
                    "fee": {"currency_code": "RUB", "value": 50.0},
                },
                "returns": {"amount": {"currency_code": "RUB", "value": -100.0}},
                "services": [{"amount": {"currency_code": "RUB", "value": 20.0}, "name": "Реклама"}],
            },
            "total": {
                "accrued": {"currency_code": "RUB", "value": 840.0},
                "closing_balance": {"currency_code": "RUB", "value": 840.0},
                "opening_balance": {"currency_code": "RUB", "value": 0.0},
                "payments": [{"currency_code": "RUB", "value": 800.0}],
            },
        }

        request = FinanceBalanceRequest(date_from="2026-05-01", date_to="2026-06-01")

        response = await api.finance_balance(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/balance",
            payload=request.model_dump()
        )

        assert isinstance(response, FinanceBalanceResponse)
        assert response.cashflows.sales.amount.value == 1000.0
        assert response.total.closing_balance.value == 840.0
        assert response.cashflows.services[0].name == "Реклама"
