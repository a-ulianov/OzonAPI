import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceMutualSettlementRequest,
    FinanceMutualSettlementResponse,
)


class TestFinanceMutualSettlement:
    """Тесты для метода finance_mutual_settlement."""

    @pytest.mark.asyncio
    async def test_finance_mutual_settlement(self, api, mock_api_request):
        """Тестирует метод finance_mutual_settlement."""

        mock_api_request.return_value = {"result": {"code": "ms-7"}}

        request = FinanceMutualSettlementRequest(date="2026-04", language="DEFAULT")

        response = await api.finance_mutual_settlement(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/mutual-settlement",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceMutualSettlementResponse)
        assert response.result.code == "ms-7"
