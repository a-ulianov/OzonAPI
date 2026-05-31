import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateRejectionReasonsListResponse


class TestProductCertificateRejectionReasonsList:
    """Тесты для метода product_certificate_rejection_reasons_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_rejection_reasons_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_rejection_reasons_list."""

        mock_api_request.return_value = {"result": [{"code": "BAD_SCAN", "name": "Плохой скан"}]}

        response = await api.product_certificate_rejection_reasons_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/rejection_reasons/list",
            payload={}
        )

        assert isinstance(response, ProductCertificateRejectionReasonsListResponse)
        assert response.result[0].code == "BAD_SCAN"
