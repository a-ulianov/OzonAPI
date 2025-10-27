import pytest

from src.ozonapi.seller.schemas.products import ProductImportInfoRequest, ProductImportInfoResponse


class TestProductImportInfo:
    """Тесты для метода product_import_info."""

    @pytest.mark.asyncio
    async def test_product_import_info(self, api, mock_api_request):
        """Тестирует метод product_import_info."""
        mock_response_data = {
            "result": {
                "items": [],
                "total": 0
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ProductImportInfoRequest(
            task_id=1234567
        )
        response = await api.product_import_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import/info",
            json=request.model_dump()
        )
        assert isinstance(response, ProductImportInfoResponse)
        assert response.result.total == 0
