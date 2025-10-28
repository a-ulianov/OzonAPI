import pytest

from src.ozonapi.seller.schemas.products import ProductPicturesInfoRequest, ProductPicturesInfoResponse


class TestProductPicturesInfo:
    """Тесты для метода product_pictures_info."""

    @pytest.mark.asyncio
    async def test_product_pictures_info(self, api, mock_api_request):
        """Тестирует метод product_pictures_info."""
        mock_response_data = {
            "items": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductPicturesInfoRequest(
            product_id=[123456789, 987654321]
        )
        response = await api.product_pictures_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="product/pictures/info",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductPicturesInfoResponse)
        assert response.items == []
