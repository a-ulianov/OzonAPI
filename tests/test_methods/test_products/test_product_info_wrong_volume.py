import pytest

from src.ozonapi.seller.schemas.products import (
    ProductInfoWrongVolumeRequest,
    ProductInfoWrongVolumeResponse,
)


class TestProductInfoWrongVolume:
    """Тесты для метода product_info_wrong_volume."""

    @pytest.mark.asyncio
    async def test_product_info_wrong_volume(self, api, mock_api_request):
        """Тестирует метод product_info_wrong_volume."""
        mock_response_data = {
            "cursor": "next-cursor-token",
            "products": [
                {
                    "product_id": 123456,
                    "sku": 987654321,
                    "offer_id": "article-1",
                    "name": "Тестовый товар",
                    "height": 100,
                    "length": 200,
                    "width": 150,
                    "weight": 500,
                },
            ],
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoWrongVolumeRequest(limit=100)
        response = await api.product_info_wrong_volume(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/wrong-volume",
            payload=request.model_dump(),
        )
        assert isinstance(response, ProductInfoWrongVolumeResponse)
        assert response.cursor == "next-cursor-token"
        assert len(response.products) == 1
        assert response.products[0].offer_id == "article-1"
        assert response.products[0].weight == 500
        assert response.products[0].sku == 987654321
