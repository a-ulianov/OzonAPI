import pytest

from src.ozonapi.seller.schemas.beta import (
    FinanceAccrualPostingsRequest,
    FinanceAccrualPostingsResponse,
)


class TestFinanceAccrualPostings:
    """Тесты для метода finance_accrual_postings."""

    @pytest.mark.asyncio
    async def test_finance_accrual_postings(self, api, mock_api_request):
        """Тестирует метод finance_accrual_postings."""

        mock_api_request.return_value = {
            "posting_accruals": [
                {
                    "posting_number": "0001-1",
                    "accruals": [
                        {
                            "accrual_date": "2026-05-15",
                            "accrued": {"amount": "100.00", "currency": "RUB"},
                            "quantity": 1,
                            "seller_price": {"amount": "120.00", "currency": "RUB"},
                            "sku": 222,
                            "type_id": 3,
                        }
                    ],
                }
            ]
        }

        request = FinanceAccrualPostingsRequest(posting_numbers=["0001-1"])

        response = await api.finance_accrual_postings(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/postings",
            payload=request.model_dump()
        )

        assert isinstance(response, FinanceAccrualPostingsResponse)
        accr = response.posting_accruals[0].accruals[0]
        assert accr.sku == 222
        assert accr.accrued.amount == "100.00"
