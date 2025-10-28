import pytest

from src.ozonapi.seller.schemas.products import ProductInfoDescriptionRequest, ProductInfoDescriptionResponse


class TestProductInfoDescription:
    """Тесты для метода product_info_description."""

    @pytest.mark.asyncio
    async def test_product_info_description(self, api, mock_api_request):
        """Тестирует метод product_info_description."""
        mock_response_data = {
            "result": {
                "id": 12345678,
                "name": "Test Product Name",
                "offer_id": "test_offer_123",
                "description": "This is a test product description"
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoDescriptionRequest(
            product_id=12345678
        )
        response = await api.product_info_description(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/description",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoDescriptionResponse)
        assert response.result.id == 12345678
        assert response.result.name == "Test Product Name"
        assert response.result.offer_id == "test_offer_123"
        assert response.result.description == "This is a test product description"