import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsAutoAddProductsUpdateProduct,
    ActionsAutoAddProductsUpdateRequest,
    ActionsAutoAddProductsUpdateResponse,
)


class TestActionsAutoAddProductsUpdate:
    """Тесты для метода actions_auto_add_products_update."""

    @pytest.mark.asyncio
    async def test_actions_auto_add_products_update(self, api, mock_api_request):
        """Тестирует метод actions_auto_add_products_update."""

        mock_api_request.return_value = {
            "updated_ids": ["313455276"],
            "rejected": [
                {"product_id": 999, "code": "REJECTED_LOW_PRICE", "reason": "Цена ниже минимальной"}
            ],
            "below_min_price": [{"key": 999, "value": 100.0}],
            "extremely_low_price": [],
            "failed_price": [],
        }

        request = ActionsAutoAddProductsUpdateRequest(
            action_id=123456,
            auto_add_date="2026-07-01T00:00:00Z",
            to_update=[
                ActionsAutoAddProductsUpdateProduct(product_id=313455276, action_price=999.0)
            ],
        )

        response = await api.actions_auto_add_products_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/update",
            payload=request.model_dump(),
        )

        assert isinstance(response, ActionsAutoAddProductsUpdateResponse)
        assert response.updated_ids == ["313455276"]
        assert response.rejected[0].code == "REJECTED_LOW_PRICE"
        assert response.below_min_price[0].key == 999
