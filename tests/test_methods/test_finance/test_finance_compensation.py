import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceCompensationRequest,
    FinanceCompensationResponse,
)


class TestFinanceCompensation:
    """Тесты для метода finance_compensation."""

    @pytest.mark.asyncio
    async def test_finance_compensation(self, api, mock_api_request):
        """Тестирует метод finance_compensation."""

        mock_api_request.return_value = {"result": {"code": "comp-1"}}

        request = FinanceCompensationRequest(date="2026-04", language="DEFAULT")

        response = await api.finance_compensation(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/compensation",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceCompensationResponse)
        assert response.result.code == "comp-1"
