import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyProductsListRequest,
    StrategyProductsListResponse,
)


class TestStrategyProductsList:
    """Тесты для метода strategy_products_list."""

    @pytest.mark.asyncio
    async def test_strategy_products_list(self, api, mock_api_request):
        """Тестирует метод strategy_products_list."""
        mock_api_request.return_value = {"result": {"product_id": ["313455276", "1318117230"]}}

        request = StrategyProductsListRequest(strategy_id="abc-123")
        response = await api.strategy_products_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyProductsListResponse)
        assert response.result.product_id == ["313455276", "1318117230"]
