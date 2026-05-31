import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateDeleteRequest,
    ProductCertificateDeleteResponse,
)


class TestProductCertificateDelete:
    """Тесты для метода product_certificate_delete."""

    @pytest.mark.asyncio
    async def test_product_certificate_delete(self, api, mock_api_request):
        """Тестирует метод product_certificate_delete."""

        mock_api_request.return_value = {"result": {"is_delete": True, "error_message": ""}}

        request = ProductCertificateDeleteRequest(certificate_id=50058)

        response = await api.product_certificate_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateDeleteResponse)
        assert response.result.is_delete is True
