import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsAutoAddProductsDeleteRequest,
    ActionsAutoAddProductsDeleteResponse,
)


class TestActionsAutoAddProductsDelete:
    """Тесты для метода actions_auto_add_products_delete."""

    @pytest.mark.asyncio
    async def test_actions_auto_add_products_delete(self, api, mock_api_request):
        """Тестирует метод actions_auto_add_products_delete."""

        mock_api_request.return_value = {"product_ids": ["313455276"]}

        request = ActionsAutoAddProductsDeleteRequest(
            action_id=123456, auto_add_date="2026-07-01T00:00:00Z", product_ids=["313455276"]
        )

        response = await api.actions_auto_add_products_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/delete",
            payload=request.model_dump(),
        )

        assert isinstance(response, ActionsAutoAddProductsDeleteResponse)
        assert response.product_ids == ["313455276"]
