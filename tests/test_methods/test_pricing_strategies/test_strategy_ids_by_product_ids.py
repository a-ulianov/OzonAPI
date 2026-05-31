import pytest

from src.ozonapi.seller.schemas.pricing_strategies import (
    StrategyIdsByProductIdsRequest,
    StrategyIdsByProductIdsResponse,
)


class TestStrategyIdsByProductIds:
    """Тесты для метода strategy_ids_by_product_ids."""

    @pytest.mark.asyncio
    async def test_strategy_ids_by_product_ids(self, api, mock_api_request):
        """Тестирует метод strategy_ids_by_product_ids."""
        mock_api_request.return_value = {
            "result": {
                "products_info": [
                    {"product_id": 313455276, "strategy_id": "abc-123"}
                ]
            }
        }

        request = StrategyIdsByProductIdsRequest(product_id=["313455276"])
        response = await api.strategy_ids_by_product_ids(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/strategy-ids-by-product-ids",
            payload=request.model_dump(),
        )
        assert isinstance(response, StrategyIdsByProductIdsResponse)
        assert response.result.products_info[0].product_id == 313455276
        assert response.result.products_info[0].strategy_id == "abc-123"
