import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsProductsDeactivateRequest,
    ActionsProductsDeactivateResponse,
)


class TestActionsProductsDeactivate:
    """Тесты для метода actions_products_deactivate."""

    @pytest.mark.asyncio
    async def test_actions_products_deactivate(self, api, mock_api_request):
        """Тестирует метод actions_products_deactivate."""
        mock_api_request.return_value = {
            "result": {"product_ids": [313455276], "rejected": []}
        }

        request = ActionsProductsDeactivateRequest(
            action_id=123456, product_ids=[313455276]
        )
        response = await api.actions_products_deactivate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/products/deactivate",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsProductsDeactivateResponse)
        assert response.result.product_ids == [313455276]
        assert response.result.rejected == []
