import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceDecompensationRequest,
    FinanceDecompensationResponse,
)


class TestFinanceDecompensation:
    """Тесты для метода finance_decompensation."""

    @pytest.mark.asyncio
    async def test_finance_decompensation(self, api, mock_api_request):
        """Тестирует метод finance_decompensation."""

        mock_api_request.return_value = {"result": {"code": "decomp-1"}}

        request = FinanceDecompensationRequest(date="2026-04", language="DEFAULT")

        response = await api.finance_decompensation(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/decompensation",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceDecompensationResponse)
        assert response.result.code == "decomp-1"
