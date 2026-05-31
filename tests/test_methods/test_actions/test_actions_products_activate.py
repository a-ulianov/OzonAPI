import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsProductsActivateRequest,
    ActionsProductsActivateProduct,
    ActionsProductsActivateResponse,
)


class TestActionsProductsActivate:
    """Тесты для метода actions_products_activate."""

    @pytest.mark.asyncio
    async def test_actions_products_activate(self, api, mock_api_request):
        """Тестирует метод actions_products_activate."""
        mock_api_request.return_value = {
            "result": {
                "product_ids": [313455276],
                "rejected": [{"product_id": 999, "reason": "Цена слишком высокая"}],
            }
        }

        request = ActionsProductsActivateRequest(
            action_id=123456,
            products=[
                ActionsProductsActivateProduct(product_id=313455276, action_price=900.0)
            ],
        )
        response = await api.actions_products_activate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/products/activate",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsProductsActivateResponse)
        assert response.result.product_ids == [313455276]
        assert response.result.rejected[0].product_id == 999
