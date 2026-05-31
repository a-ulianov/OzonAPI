import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyCreateRequest,
    StrategyCreateResponse,
    StrategyCompetitor,
)


class TestStrategyCreate:
    """Тесты для метода strategy_create."""

    @pytest.mark.asyncio
    async def test_strategy_create(self, api, mock_api_request):
        """Тестирует метод strategy_create."""
        mock_api_request.return_value = {"result": {"strategy_id": "abc-123"}}

        request = StrategyCreateRequest(
            strategy_name="Моя стратегия",
            competitors=[StrategyCompetitor(competitor_id=1, coefficient=0.9)],
        )
        response = await api.strategy_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyCreateResponse)
        assert response.result.strategy_id == "abc-123"

        # Коэффициент допустим только в диапазоне 0.5–1.2.
        with pytest.raises(ValueError):
            StrategyCompetitor(competitor_id=1, coefficient=0.4)
        with pytest.raises(ValueError):
            StrategyCompetitor(competitor_id=1, coefficient=1.3)
