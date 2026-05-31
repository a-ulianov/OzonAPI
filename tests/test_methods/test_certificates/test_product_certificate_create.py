import aiohttp
import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateCreateRequest,
    ProductCertificateCreateResponse,
)


class TestProductCertificateCreate:
    """Тесты для метода product_certificate_create."""

    @pytest.mark.asyncio
    async def test_product_certificate_create(self, api, mock_api_request):
        """Тестирует метод product_certificate_create (multipart/form-data)."""

        mock_api_request.return_value = {"id": 50058}

        request = ProductCertificateCreateRequest(
            files=[b"%PDF-1.4 cert"],
            name="Сертификат",
            number="RU-123",
            type_code="certificate",
            issue_date="2026-01-01T00:00:00Z"
        )

        response = await api.product_certificate_create(request)

        mock_api_request.assert_called_once()
        kwargs = mock_api_request.call_args.kwargs
        assert kwargs["method"] == "post"
        assert kwargs["api_version"] == "v1"
        assert kwargs["endpoint"] == "product/certificate/create"
        assert isinstance(kwargs["form_data"], aiohttp.FormData)

        assert isinstance(response, ProductCertificateCreateResponse)
        assert response.id == 50058
