import pytest

from src.ozonapi.seller.schemas.beta import (
    FinanceAccrualByDayRequest,
    FinanceAccrualByDayResponse,
)


class TestFinanceAccrualByDay:
    """Тесты для метода finance_accrual_by_day."""

    @pytest.mark.asyncio
    async def test_finance_accrual_by_day(self, api, mock_api_request):
        """Тестирует метод finance_accrual_by_day."""

        mock_api_request.return_value = {
            "last_id": "abc",
            "accruals": [
                {
                    "accrued_category": "SALE",
                    "date": "2026-05-15",
                    "total_amount": {"amount": "100.00", "currency": "RUB"},
                    "type_id": 3,
                    "unit_number": "U-1",
                    "posting": {
                        "delivery_schema": "FBS",
                        "delivery_speed": 2,
                        "products": [
                            {
                                "sku": 222,
                                "commission": {
                                    "commission": {"amount": "10.00", "currency": "RUB"},
                                    "commission_ratio": "0.1",
                                },
                                "delivery": {
                                    "total_accrued": {"amount": "5.00", "currency": "RUB"},
                                    "services": [
                                        {"accrued": {"amount": "5.00", "currency": "RUB"}, "type_id": 9}
                                    ],
                                },
                            }
                        ],
                    },
                }
            ],
        }

        request = FinanceAccrualByDayRequest(date="2026-05-15")

        response = await api.finance_accrual_by_day(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/by-day",
            payload=request.model_dump()
        )

        assert isinstance(response, FinanceAccrualByDayResponse)
        item = response.accruals[0]
        assert item.total_amount.amount == "100.00"
        assert item.posting.products[0].sku == 222
        assert item.posting.products[0].commission.commission_ratio == "0.1"
        assert item.posting.products[0].delivery.total_accrued.amount == "5.00"
