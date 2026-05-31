import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyProductInfoRequest,
    StrategyProductInfoResponse,
)


class TestStrategyProductInfo:
    """Тесты для метода strategy_product_info."""

    @pytest.mark.asyncio
    async def test_strategy_product_info(self, api, mock_api_request):
        """Тестирует метод strategy_product_info."""
        mock_api_request.return_value = {
            "result": {
                "is_enabled": True,
                "strategy_id": "abc-123",
                "strategy_product_price": 1000,
                "price_downloaded_at": "2024-01-01T00:00:00Z",
                "strategy_competitor_id": 1,
                "strategy_competitor_product_url": "https://example.com/p/1",
            }
        }

        request = StrategyProductInfoRequest(product_id=313455276)
        response = await api.strategy_product_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/product/info",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyProductInfoResponse)
        assert response.result.is_enabled is True
        assert response.result.strategy_id == "abc-123"
        assert response.result.strategy_product_price == 1000
