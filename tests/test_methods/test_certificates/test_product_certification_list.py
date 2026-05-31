import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificationListRequest,
    ProductCertificationListResponse,
)


class TestProductCertificationList:
    """Тесты для метода product_certification_list."""

    @pytest.mark.asyncio
    async def test_product_certification_list(self, api, mock_api_request):
        """Тестирует метод product_certification_list."""

        mock_api_request.return_value = {
            "total": 1,
            "certification": [
                {"category_id": 10, "category_name": "Игрушки", "type_id": 5, "is_required": True}
            ]
        }

        request = ProductCertificationListRequest(page=1, page_size=100)

        response = await api.product_certification_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="product/certification/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificationListResponse)
        assert response.certification[0].category_id == 10
