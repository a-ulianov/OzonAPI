import pytest

from src.ozonapi.seller.schemas.products import ProductImportBySkuRequest, ProductImportBySkuResponse


class TestProductImportBySku:
    """Тесты для метода product_import_by_sku."""

    @pytest.mark.asyncio
    async def test_product_import_by_sku(self, api, mock_api_request):
        """Тестирует метод product_import_by_sku."""
        mock_response_data = {
            "task_id": 123456789,
            "unmatched_sku_list": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductImportBySkuRequest(
            items=[]
        )
        response = await api.product_import_by_sku(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import-by-sku",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductImportBySkuResponse)
        assert response.task_id == 123456789
