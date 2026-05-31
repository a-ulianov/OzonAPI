import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateBindRequest,
    ProductCertificateBindResponse,
)


class TestProductCertificateBind:
    """Тесты для метода product_certificate_bind."""

    @pytest.mark.asyncio
    async def test_product_certificate_bind(self, api, mock_api_request):
        """Тестирует метод product_certificate_bind."""

        mock_api_request.return_value = {"result": True}

        request = ProductCertificateBindRequest(certificate_id=50058, product_id=[123456])

        response = await api.product_certificate_bind(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/bind",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateBindResponse)
        assert response.result is True
