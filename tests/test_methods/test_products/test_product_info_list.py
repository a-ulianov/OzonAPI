import pytest

from src.ozonapi.seller.schemas.products import ProductInfoListRequest, ProductInfoListResponse


class TestProductInfoList:
    """Тесты для метода product_info_list."""

    @pytest.mark.asyncio
    async def test_product_info_list(self, api, mock_api_request):
        """Тестирует метод product_info_list."""
        mock_response_data = {
            "items": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoListRequest(
            product_id=[123456789, 987654321]
        )
        response = await api.product_info_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/info/list",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoListResponse)
        assert response.items == []

