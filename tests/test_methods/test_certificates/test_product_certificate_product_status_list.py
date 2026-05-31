import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateProductStatusListResponse


class TestProductCertificateProductStatusList:
    """Тесты для метода product_certificate_product_status_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_product_status_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_product_status_list."""

        mock_api_request.return_value = {"result": [{"code": "OK", "name": "Привязан"}]}

        response = await api.product_certificate_product_status_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/product_status/list",
            payload={}
        )

        assert isinstance(response, ProductCertificateProductStatusListResponse)
        assert response.result[0].code == "OK"
