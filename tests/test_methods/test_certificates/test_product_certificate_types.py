import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateTypesResponse


class TestProductCertificateTypes:
    """Тесты для метода product_certificate_types."""

    @pytest.mark.asyncio
    async def test_product_certificate_types(self, api, mock_api_request):
        """Тестирует метод product_certificate_types."""

        mock_api_request.return_value = {"result": [{"name": "Сертификат", "value": "certificate"}]}

        response = await api.product_certificate_types()

        mock_api_request.assert_called_once_with(
            method="get",
            api_version="v1",
            endpoint="product/certificate/types",
            payload={}
        )

        assert isinstance(response, ProductCertificateTypesResponse)
        assert response.result[0].value == "certificate"
