import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyUpdateRequest,
    StrategyUpdateResponse,
    StrategyCompetitor,
)


class TestStrategyUpdate:
    """Тесты для метода strategy_update."""

    @pytest.mark.asyncio
    async def test_strategy_update(self, api, mock_api_request):
        """Тестирует метод strategy_update."""
        mock_api_request.return_value = {}

        request = StrategyUpdateRequest(
            strategy_id="abc-123",
            strategy_name="Новое имя",
            competitors=[StrategyCompetitor(competitor_id=1, coefficient=1.0)],
        )
        response = await api.strategy_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/update",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyUpdateResponse)
