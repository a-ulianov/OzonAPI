import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyProductsAddRequest,
    StrategyProductsAddResponse,
)


class TestStrategyProductsAdd:
    """Тесты для метода strategy_products_add."""

    @pytest.mark.asyncio
    async def test_strategy_products_add(self, api, mock_api_request):
        """Тестирует метод strategy_products_add."""
        mock_api_request.return_value = {
            "result": {
                "errors": [
                    {"code": "ERR", "error": "Текст ошибки", "product_id": 313455276}
                ],
                "failed_product_count": 1,
            }
        }

        request = StrategyProductsAddRequest(
            strategy_id="abc-123", product_id=["313455276"]
        )
        response = await api.strategy_products_add(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/add",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyProductsAddResponse)
        assert response.result.failed_product_count == 1
        assert response.result.errors[0].product_id == 313455276
