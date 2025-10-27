import pytest

from src.ozonapi.seller.schemas.products import ProductArchiveRequest, ProductArchiveResponse


class TestProductArchive:
    """Тесты для метода product_archive."""

    @pytest.mark.asyncio
    async def test_product_archive(self, api, mock_api_request):
        """Тестирует метод product_archive."""
        mock_response_data = {
            "result": True
        }
        mock_api_request.return_value = mock_response_data

        request = ProductArchiveRequest(
            product_id=[123456, 789012]
        )
        response = await api.product_archive(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/archive",
            json=request.model_dump()
        )
        assert isinstance(response, ProductArchiveResponse)
        assert response.result is True
