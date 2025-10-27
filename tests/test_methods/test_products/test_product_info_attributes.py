import pytest

from src.ozonapi.seller.schemas.products import ProductInfoAttributesRequest, ProductInfoAttributesResponse


class TestProductInfoAttributes:
    """Тесты для метода product_info_attributes."""

    @pytest.mark.asyncio
    async def test_product_info_attributes(self, api, mock_api_request):
        """Тестирует метод product_info_attributes."""
        mock_response_data = {
            "result": [],
            "last_id": "test_last_id",
            "total": 0
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoAttributesRequest()
        response = await api.product_info_attributes(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/attributes",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoAttributesResponse)
        assert response.total == 0
