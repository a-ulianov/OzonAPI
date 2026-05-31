import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsProductsRequest,
    ActionsProductsResponse,
)


class TestActionsProducts:
    """Тесты для метода actions_products."""

    @pytest.mark.asyncio
    async def test_actions_products(self, api, mock_api_request):
        """Тестирует метод actions_products."""
        mock_api_request.return_value = {
            "result": {
                "products": [
                    {
                        "id": 313455276,
                        "price": 1000.0,
                        "action_price": 900.0,
                        "stock": 5,
                        "sku": 635548518,
                    }
                ],
                "total": 1,
            }
        }

        request = ActionsProductsRequest(action_id=123456, limit=100)
        response = await api.actions_products(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/products",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsProductsResponse)
        assert response.result.total == 1
        assert response.result.products[0].id == 313455276
