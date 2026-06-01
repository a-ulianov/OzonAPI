import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsAutoAddProductsListRequest,
    ActionsAutoAddProductsListResponse,
)


class TestActionsAutoAddProductsList:
    """Тесты для метода actions_auto_add_products_list."""

    @pytest.mark.asyncio
    async def test_actions_auto_add_products_list(self, api, mock_api_request):
        """Тестирует метод actions_auto_add_products_list."""

        mock_api_request.return_value = {
            "products": [
                {
                    "product_id": 313455276,
                    "sku": 1234567890,
                    "offer_id": "ART-1",
                    "currency": "RUB",
                    "action_price_to_auto_add": 900.0,
                    "add_mode": "AUTO",
                }
            ],
            "total": 1,
        }

        request = ActionsAutoAddProductsListRequest(
            action_id=123456, auto_add_date="2026-07-01T00:00:00Z", limit=100
        )

        response = await api.actions_auto_add_products_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/list",
            payload=request.model_dump(),
        )

        assert isinstance(response, ActionsAutoAddProductsListResponse)
        assert response.total == 1
        assert response.products[0].add_mode == "AUTO"
