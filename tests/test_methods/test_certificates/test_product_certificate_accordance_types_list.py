import pytest

from src.ozonapi.seller.schemas.certificates import ProductCertificateAccordanceTypesListResponse


class TestProductCertificateAccordanceTypesList:
    """Тесты для метода product_certificate_accordance_types_list."""

    @pytest.mark.asyncio
    async def test_product_certificate_accordance_types_list(self, api, mock_api_request):
        """Тестирует метод product_certificate_accordance_types_list."""

        mock_api_request.return_value = {
            "result": {
                "base": [{"code": "gost", "title": "ГОСТ"}],
                "hazard": [{"code": "haz", "title": "Опасный"}]
            }
        }

        response = await api.product_certificate_accordance_types_list()

        mock_api_request.assert_called_once_with(
            method="get",
            api_version="v2",
            endpoint="product/certificate/accordance-types/list",
            payload={}
        )

        assert isinstance(response, ProductCertificateAccordanceTypesListResponse)
        assert response.result.base[0].code == "gost"
