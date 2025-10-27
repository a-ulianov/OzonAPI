import pytest

from src.ozonapi.seller.schemas.products import ProductsDeleteRequest, ProductsDeleteResponse


class TestProductDelete:
    """Тесты для метода products_delete."""

    @pytest.mark.asyncio
    async def test_products_delete(self, api, mock_api_request):
        """Тестирует метод products_delete."""
        mock_response_data = {
            "status": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductsDeleteRequest(
            products=[]
        )
        response = await api.products_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="products/delete",
            json=request.model_dump()
        )
        assert isinstance(response, ProductsDeleteResponse)
        assert response.status == []
