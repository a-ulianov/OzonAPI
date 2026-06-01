import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsProductsCandidatesRequest,
    SellerActionsProductsCandidatesResponse,
)


class TestSellerActionsProductsCandidates:
    """Тесты для метода seller_actions_products_candidates."""

    @pytest.mark.asyncio
    async def test_seller_actions_products_candidates(self, api, mock_api_request):
        """Тестирует метод seller_actions_products_candidates."""

        mock_api_request.return_value = {
            "cursor": '{"last_used_sku":1807538652}',
            "has_next": True,
            "products": [
                {
                    "product_id": 313455276,
                    "offer_id": "ART-1",
                    "name": "Товар",
                    "price": 1000.0,
                    "base_price": 1200.0,
                    "action_price": 900.0,
                    "discount_percent": 10.0,
                    "is_active": False,
                    "currency": "RUB",
                    "quant_size": 1,
                    "quant_type": "GENERAL",
                    "sku": [1807538302],
                }
            ],
        }

        request = SellerActionsProductsCandidatesRequest(action_id=123456, limit=100)

        response = await api.seller_actions_products_candidates(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/candidates",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsProductsCandidatesResponse)
        assert response.cursor == '{"last_used_sku":1807538652}'
        assert response.has_next is True
        assert response.products[0].product_id == 313455276
        assert response.products[0].sku == [1807538302]
