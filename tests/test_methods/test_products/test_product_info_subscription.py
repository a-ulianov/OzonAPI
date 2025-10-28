import pytest

from src.ozonapi.seller.schemas.products import ProductInfoSubscriptionRequest, ProductInfoSubscriptionResponse


class TestProductInfoSubscription:
    """Тесты для метода product_info_subscription."""

    @pytest.mark.asyncio
    async def test_product_info_subscription(self, api, mock_api_request):
        """Тестирует метод product_info_subscription."""
        mock_response_data = {
            "result": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoSubscriptionRequest(
            skus=[123456789, 987654321]
        )
        response = await api.product_info_subscription(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/subscription",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoSubscriptionResponse)
        assert response.result == []
