import pytest

from src.ozonapi.seller.schemas.products import ProductAttributesUpdateRequest, ProductAttributesUpdateResponse


class TestProductAttributesUpdate:
    """Тесты для метода product_attributes_update."""

    @pytest.mark.asyncio
    async def test_product_attributes_update(self, api, mock_api_request):
        """Тестирует метод product_attributes_update."""
        mock_response_data = {
            "task_id": 123456789
        }
        mock_api_request.return_value = mock_response_data

        request = ProductAttributesUpdateRequest(
            items=[]
        )
        response = await api.product_attributes_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/attributes/update",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductAttributesUpdateResponse)
        assert response.task_id == 123456789
