import pytest

from src.ozonapi.seller.schemas.beta import (
    FinanceAccrualTypesRequest,
    FinanceAccrualTypesResponse,
)


class TestFinanceAccrualTypes:
    """Тесты для метода finance_accrual_types."""

    @pytest.mark.asyncio
    async def test_finance_accrual_types(self, api, mock_api_request):
        """Тестирует метод finance_accrual_types."""

        mock_api_request.return_value = {
            "accrual_types": [
                {"id": 3, "name": "Комиссия за продажу", "description": "Описание"}
            ]
        }

        request = FinanceAccrualTypesRequest()

        response = await api.finance_accrual_types(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/types",
            payload=request.model_dump()
        )

        assert isinstance(response, FinanceAccrualTypesResponse)
        assert response.accrual_types[0].id == 3
        assert response.accrual_types[0].name == "Комиссия за продажу"
