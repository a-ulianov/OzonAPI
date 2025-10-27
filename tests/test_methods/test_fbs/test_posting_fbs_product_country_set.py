import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSProductCountrySetResponse


class TestPostingFBSProductCountrySet:
    """Тесты для метода posting_fbs_product_country_set."""

    @pytest.mark.asyncio
    async def test_posting_fbs_product_country_set(self, api, mock_api_request):
        """Тестирует метод posting_fbs_product_country_set."""

        mock_response_data = {
            "product_id": 180550365,
            "is_gtd_needed": True
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_country_set import (
            PostingFBSProductCountrySetRequest
        )

        request = PostingFBSProductCountrySetRequest(
            posting_number="57195475-0050-3",
            product_id=180550365,
            country_iso_code="NO"
        )

        response = await api.posting_fbs_product_country_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/set",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSProductCountrySetResponse)
        assert response.product_id == 180550365
        assert response.is_gtd_needed is True
