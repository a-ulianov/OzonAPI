import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateInfoRequest,
    ProductCertificateInfoResponse,
)


class TestProductCertificateInfo:
    """Тесты для метода product_certificate_info."""

    @pytest.mark.asyncio
    async def test_product_certificate_info(self, api, mock_api_request):
        """Тестирует метод product_certificate_info."""

        mock_api_request.return_value = {
            "result": {
                "certificate_id": 50058,
                "certificate_number": "RU-123",
                "status_code": "ACTIVE",
                "products_count": 3
            }
        }

        request = ProductCertificateInfoRequest(certificate_number="RU-123")

        response = await api.product_certificate_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateInfoResponse)
        assert response.result.certificate_id == 50058
        assert response.result.products_count == 3
