import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyDeleteRequest,
    StrategyDeleteResponse,
)


class TestStrategyDelete:
    """Тесты для метода strategy_delete."""

    @pytest.mark.asyncio
    async def test_strategy_delete(self, api, mock_api_request):
        """Тестирует метод strategy_delete."""
        mock_api_request.return_value = {}

        request = StrategyDeleteRequest(strategy_id="abc-123")
        response = await api.strategy_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyDeleteResponse)
