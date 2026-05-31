import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceRealizationRequest,
    FinanceRealizationResponse,
)


class TestFinanceRealization:
    """Тесты для метода finance_realization."""

    @pytest.mark.asyncio
    async def test_finance_realization(self, api, mock_api_request):
        """Тестирует метод finance_realization."""

        mock_api_request.return_value = {
            "result": {
                "header": {"number": "12345", "doc_amount": 1500.0},
                "rows": [
                    {
                        "rowNumber": 1,
                        "item": {"sku": 111, "offer_id": "art-1", "name": "Товар"},
                        "delivery_commission": {"amount": 100.0, "quantity": 2},
                        "commission_ratio": 0.15,
                    }
                ],
            }
        }

        request = FinanceRealizationRequest(month=4, year=2026)

        response = await api.finance_realization(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="finance/realization",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceRealizationResponse)
        assert response.result.header.number == "12345"
        assert response.result.rows[0].row_number == 1
        assert response.result.rows[0].item.sku == 111
