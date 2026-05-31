import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsRfbsReturnMoneyRequest,
    ReturnsRfbsReturnMoneyResponse,
)


class TestReturnsRfbsReturnMoney:
    """Тесты для метода returns_rfbs_return_money."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_return_money(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_return_money."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsReturnMoneyRequest(return_id=12345, return_for_back_way=50)

        response = await api.returns_rfbs_return_money(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/return-money",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsReturnMoneyResponse)
