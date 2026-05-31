import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyStatusRequest,
    StrategyStatusResponse,
)


class TestStrategyStatus:
    """Тесты для метода strategy_status."""

    @pytest.mark.asyncio
    async def test_strategy_status(self, api, mock_api_request):
        """Тестирует метод strategy_status."""
        mock_api_request.return_value = {}

        request = StrategyStatusRequest(strategy_id="abc-123", enabled=True)
        response = await api.strategy_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/status",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyStatusResponse)
