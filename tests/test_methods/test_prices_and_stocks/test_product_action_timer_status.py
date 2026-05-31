import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductActionTimerStatusRequest,
    ProductActionTimerStatusResponse,
)


class TestProductActionTimerStatus:
    """Тесты для метода product_action_timer_status."""

    @pytest.mark.asyncio
    async def test_product_action_timer_status(self, api, mock_api_request):
        """Тестирует метод product_action_timer_status."""
        mock_response_data = {
            "statuses": [
                {
                    "expired_at": "2024-01-01T00:00:00Z",
                    "min_price_for_auto_actions_enabled": True,
                    "product_id": 313455276
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ProductActionTimerStatusRequest(product_ids=["313455276"])
        response = await api.product_action_timer_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/action/timer/status",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductActionTimerStatusResponse)
        assert len(response.statuses) == 1
        assert response.statuses[0].product_id == 313455276
        assert response.statuses[0].min_price_for_auto_actions_enabled is True
        assert response.statuses[0].expired_at is not None
