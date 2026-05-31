import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyInfoRequest,
    StrategyInfoResponse,
)


class TestStrategyInfo:
    """Тесты для метода strategy_info."""

    @pytest.mark.asyncio
    async def test_strategy_info(self, api, mock_api_request):
        """Тестирует метод strategy_info."""
        mock_api_request.return_value = {
            "result": {
                "competitors": [{"competitor_id": 1, "coefficient": 0.9}],
                "enabled": True,
                "name": "Моя стратегия",
                "type": "COMP_PRICE",
                "update_type": "strategyCreated",
            }
        }

        request = StrategyInfoRequest(strategy_id="abc-123")
        response = await api.strategy_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/info",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyInfoResponse)
        assert response.result.enabled is True
        assert response.result.name == "Моя стратегия"
        assert response.result.competitors[0].competitor_id == 1
