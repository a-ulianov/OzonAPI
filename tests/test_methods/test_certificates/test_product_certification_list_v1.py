import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificationListV1Request,
    ProductCertificationListV1Response,
)


class TestProductCertificationListV1:
    """Тесты для метода product_certification_list_v1."""

    @pytest.mark.asyncio
    async def test_product_certification_list_v1(self, api, mock_api_request):
        """Тестирует метод product_certification_list_v1."""

        mock_api_request.return_value = {
            "result": {
                "total": 1,
                "certification": [{"category_name": "Игрушки", "is_required": True}]
            }
        }

        request = ProductCertificationListV1Request(page=1, page_size=100)

        response = await api.product_certification_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certification/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificationListV1Response)
        assert response.result.certification[0].is_required is True
