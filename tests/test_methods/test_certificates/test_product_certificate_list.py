import pytest

from src.ozonapi.seller.schemas.certificates import (
    ProductCertificateListRequest,
    ProductCertificateListResponse,
)


class TestProductCertificateList:
    """Тесты для метода product_certificate_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_list."""

        mock_api_request.return_value = {
            "result": {
                "page_count": 1,
                "certificates": [{"certificate_id": 50058, "certificate_number": "RU-123", "status_code": "ACTIVE"}]
            }
        }

        request = ProductCertificateListRequest(page=1, page_size=100)

        response = await api.product_certificate_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/certificate/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductCertificateListResponse)
        assert response.result.certificates[0].certificate_id == 50058
