import pytest

from src.ozonapi.seller.schemas.products import ProductImportRequest, ProductImportResponse


class TestProductImport:
    """Тесты для метода product_import."""

    @pytest.mark.asyncio
    async def test_product_import(self, api, mock_api_request):
        """Тестирует метод product_import."""
        mock_response_data = {
            "result": {
                "task_id": 123456789
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ProductImportRequest(
            items=[]
        )
        response = await api.product_import(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/import",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductImportResponse)
        assert response.result.task_id == 123456789
