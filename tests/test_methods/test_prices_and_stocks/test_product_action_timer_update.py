import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductActionTimerUpdateRequest,
    ProductActionTimerUpdateResponse,
)


class TestProductActionTimerUpdate:
    """Тесты для метода product_action_timer_update."""

    @pytest.mark.asyncio
    async def test_product_action_timer_update(self, api, mock_api_request):
        """Тестирует метод product_action_timer_update."""
        mock_api_request.return_value = {}

        request = ProductActionTimerUpdateRequest(product_ids=["313455276"])
        response = await api.product_action_timer_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/action/timer/update",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductActionTimerUpdateResponse)

        # Тест на обязательность хотя бы одного идентификатора
        with pytest.raises(ValueError):
            ProductActionTimerUpdateRequest(product_ids=[])
