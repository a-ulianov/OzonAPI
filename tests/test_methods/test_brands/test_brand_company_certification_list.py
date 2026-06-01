import pytest

from src.ozonapi.seller.schemas.brands import (
    BrandCompanyCertificationListRequest,
    BrandCompanyCertificationListResponse,
)


class TestBrandCompanyCertificationList:
    """Тесты для метода brand_company_certification_list."""

    @pytest.mark.asyncio
    async def test_brand_company_certification_list(self, api, mock_api_request):
        """Тестирует метод brand_company_certification_list."""
        mock_response_data = {
            "result": {
                "brand_certification": [
                    {"brand_name": "Brand A", "has_certificate": True},
                    {"brand_name": "Brand B", "has_certificate": False},
                ],
                "total": 2,
            }
        }
        mock_api_request.return_value = mock_response_data

        request = BrandCompanyCertificationListRequest(page=1, page_size=100)
        response = await api.brand_company_certification_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="brand/company-certification/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, BrandCompanyCertificationListResponse)
        assert response.result.total == 2
        assert len(response.result.brand_certification) == 2
        assert response.result.brand_certification[0].brand_name == "Brand A"
        assert response.result.brand_certification[0].has_certificate is True
        assert response.result.brand_certification[1].has_certificate is False
