import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateAccordanceTypesResponse


class TestProductCertificateAccordanceTypes:
    """Тесты для метода product_certificate_accordance_types."""

    @pytest.mark.asyncio
    async def test_product_certificate_accordance_types(self, api, mock_api_request):
        """Тестирует метод product_certificate_accordance_types."""

        mock_api_request.return_value = {"result": [{"name": "Декларация", "value": "declaration"}]}

        response = await api.product_certificate_accordance_types()

        mock_api_request.assert_called_once_with(
            method="get",
            api_version="v1",
            endpoint="product/certificate/accordance-types",
            payload={}
        )

        assert isinstance(response, ProductCertificateAccordanceTypesResponse)
        assert response.result[0].value == "declaration"
