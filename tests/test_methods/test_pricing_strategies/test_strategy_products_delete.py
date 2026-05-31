import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyProductsDeleteRequest,
    StrategyProductsDeleteResponse,
)


class TestStrategyProductsDelete:
    """Тесты для метода strategy_products_delete."""

    @pytest.mark.asyncio
    async def test_strategy_products_delete(self, api, mock_api_request):
        """Тестирует метод strategy_products_delete."""
        mock_api_request.return_value = {"result": {"failed_product_count": 0}}

        request = StrategyProductsDeleteRequest(product_id=["313455276"])
        response = await api.strategy_products_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyProductsDeleteResponse)
        assert response.result.failed_product_count == 0
