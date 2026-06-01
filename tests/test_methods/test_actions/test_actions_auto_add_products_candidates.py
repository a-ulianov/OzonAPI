import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsAutoAddProductsCandidatesRequest,
    ActionsAutoAddProductsCandidatesResponse,
)


class TestActionsAutoAddProductsCandidates:
    """Тесты для метода actions_auto_add_products_candidates."""

    @pytest.mark.asyncio
    async def test_actions_auto_add_products_candidates(self, api, mock_api_request):
        """Тестирует метод actions_auto_add_products_candidates."""

        mock_api_request.return_value = {
            "products": [
                {
                    "product_id": 313455276,
                    "sku": 1234567890,
                    "offer_id": "ART-1",
                    "name": "Товар",
                    "currency": "RUB",
                    "price": 1000.0,
                    "action_price_to_auto_add": 900.0,
                    "min_action_quantity": 1,
                    "quantity_to_auto_add": 5,
                }
            ],
            "total": 1,
        }

        request = ActionsAutoAddProductsCandidatesRequest(
            action_id=123456, auto_add_date="2026-07-01T00:00:00Z", limit=100
        )

        response = await api.actions_auto_add_products_candidates(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/candidates",
            payload=request.model_dump(),
        )

        assert isinstance(response, ActionsAutoAddProductsCandidatesResponse)
        assert response.total == 1
        assert response.products[0].product_id == 313455276
        assert response.products[0].sku == 1234567890
