import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceRealizationByDayRequest,
    FinanceRealizationByDayResponse,
)


class TestFinanceRealizationByDay:
    """Тесты для метода finance_realization_by_day."""

    @pytest.mark.asyncio
    async def test_finance_realization_by_day(self, api, mock_api_request):
        """Тестирует метод finance_realization_by_day."""

        mock_api_request.return_value = {
            "rows": [
                {
                    "rowNumber": 1,
                    "commission_ratio": 0.15,
                    "seller_price_per_instance": 1000.0,
                    "item": {"sku": 1234567890, "name": "Товар", "offer_id": "ART-1"},
                    "delivery_commission": {"amount": 1000.0, "quantity": 1, "total": 850.0},
                    "return_commission": {"amount": 0.0, "quantity": 0, "total": 0.0},
                }
            ]
        }

        request = FinanceRealizationByDayRequest(day=1, month=6, year=2026)

        response = await api.finance_realization_by_day(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/realization/by-day",
            payload=request.model_dump(),
        )

        assert isinstance(response, FinanceRealizationByDayResponse)
        assert response.rows[0].row_number == 1
        assert response.rows[0].item.sku == 1234567890
        assert response.rows[0].delivery_commission.total == 850.0
