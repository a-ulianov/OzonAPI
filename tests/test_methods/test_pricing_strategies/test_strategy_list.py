import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyListRequest,
    StrategyListResponse,
)


class TestStrategyList:
    """Тесты для метода strategy_list."""

    @pytest.mark.asyncio
    async def test_strategy_list(self, api, mock_api_request):
        """Тестирует метод strategy_list."""
        mock_api_request.return_value = {
            "strategies": [
                {
                    "id": "abc-123",
                    "name": "Моя стратегия",
                    "type": "COMP_PRICE",
                    "enabled": True,
                    "update_type": "strategyCreated",
                    "updated_at": "2024-01-01T00:00:00Z",
                    "competitors_count": 2,
                    "products_count": 10,
                }
            ],
            "total": 1,
        }

        request = StrategyListRequest(limit=50, page=1)
        response = await api.strategy_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyListResponse)
        assert response.total == 1
        assert response.strategies[0].id == "abc-123"
        assert response.strategies[0].products_count == 10

        with pytest.raises(ValueError):
            StrategyListRequest(limit=0, page=1)
