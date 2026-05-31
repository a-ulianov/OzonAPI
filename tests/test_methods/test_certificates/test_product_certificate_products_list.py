import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateProductsListRequest,
    ProductCertificateProductsListResponse,
)


class TestProductCertificateProductsList:
    """Тесты для метода product_certificate_products_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_products_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_products_list."""

        mock_api_request.return_value = {
            "result": {
                "count": 1,
                "items": [{"product_id": 123456, "product_status_code": "OK"}]
            }
        }

        request = ProductCertificateProductsListRequest(certificate_id=50058, page=1, page_size=100)

        response = await api.product_certificate_products_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/products/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateProductsListResponse)
        assert response.result.items[0].product_id == 123456
