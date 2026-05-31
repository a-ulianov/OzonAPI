import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyCompetitorsListRequest,
    StrategyCompetitorsListResponse,
)


class TestStrategyCompetitorsList:
    """Тесты для метода strategy_competitors_list."""

    @pytest.mark.asyncio
    async def test_strategy_competitors_list(self, api, mock_api_request):
        """Тестирует метод strategy_competitors_list."""
        mock_api_request.return_value = {
            "competitor": [{"id": 1, "name": "Конкурент"}],
            "total": 1,
        }

        request = StrategyCompetitorsListRequest(limit=50, page=1)
        response = await api.strategy_competitors_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/competitors/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyCompetitorsListResponse)
        assert response.total == 1
        assert response.competitor[0].id == 1
        assert response.competitor[0].name == "Конкурент"

        with pytest.raises(ValueError):
            StrategyCompetitorsListRequest(limit=51, page=1)
        with pytest.raises(ValueError):
            StrategyCompetitorsListRequest(limit=10, page=0)
