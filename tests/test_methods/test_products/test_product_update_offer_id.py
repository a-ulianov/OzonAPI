import pytest

from src.ozonapi.seller.schemas.products import ProductUpdateOfferIdRequest, ProductUpdateOfferIdResponse


class TestProductUpdateOfferId:
    """Тесты для метода product_update_offer_id."""

    @pytest.mark.asyncio
    async def test_product_update_offer_id(self, api, mock_api_request):
        """Тестирует метод product_update_offer_id."""
        mock_response_data = {
            "errors": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductUpdateOfferIdRequest(
            update_offer_id=[]
        )
        response = await api.product_update_offer_id(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/update/offer-id",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductUpdateOfferIdResponse)
        assert response.errors == []
