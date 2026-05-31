import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateUnbindRequest,
    ProductCertificateUnbindResponse,
)


class TestProductCertificateUnbind:
    """Тесты для метода product_certificate_unbind."""

    @pytest.mark.asyncio
    async def test_product_certificate_unbind(self, api, mock_api_request):
        """Тестирует метод product_certificate_unbind."""

        mock_api_request.return_value = {
            "result": [{"product_id": 123456, "updated": True, "error": ""}]
        }

        request = ProductCertificateUnbindRequest(certificate_id=50058, product_id=["123456"])

        response = await api.product_certificate_unbind(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/unbind",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateUnbindResponse)
        assert response.result[0].updated is True
