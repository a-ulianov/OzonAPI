import pytest

from src.ozonapi.seller.schemas.products import ProductUnarchiveRequest, ProductUnarchiveResponse


class TestProductUnarchive:
    """Тесты для метода product_unarchive."""

    @pytest.mark.asyncio
    async def test_product_unarchive(self, api, mock_api_request):
        """Тестирует метод product_unarchive."""
        mock_response_data = {
            "result": True
        }
        mock_api_request.return_value = mock_response_data

        request = ProductUnarchiveRequest(
            product_id=[125529926]
        )
        response = await api.product_unarchive(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/unarchive",
            json=request.model_dump()
        )
        assert isinstance(response, ProductUnarchiveResponse)
        assert response.result is True
