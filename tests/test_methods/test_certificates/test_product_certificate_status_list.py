import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateStatusListResponse


class TestProductCertificateStatusList:
    """Тесты для метода product_certificate_status_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_status_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_status_list."""

        mock_api_request.return_value = {"result": [{"code": "ACTIVE", "name": "Действует"}]}

        response = await api.product_certificate_status_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/status/list",
            payload={}
        )

        assert isinstance(response, ProductCertificateStatusListResponse)
        assert response.result[0].code == "ACTIVE"
