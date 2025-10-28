import pytest

from src.ozonapi.seller.schemas.products import ProductListRequest, ProductListResponse


class TestProductList:
    """Тесты для метода product_list."""

    @pytest.mark.asyncio
    async def test_product_list(self, api, mock_api_request):
        """Тестирует метод product_list."""
        mock_response_data = {
            "result": {
                "items": [],
                "last_id": "test_last_id",
                "total": 0
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ProductListRequest()
        response = await api.product_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/list",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductListResponse)
        assert response.result.total == 0
