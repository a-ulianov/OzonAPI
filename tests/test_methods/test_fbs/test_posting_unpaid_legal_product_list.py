import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingUnpaidLegalProductListRequest,
    PostingUnpaidLegalProductListResponse,
)


class TestPostingUnpaidLegalProductList:
    """Тесты для метода posting_unpaid_legal_product_list."""

    @pytest.mark.asyncio
    async def test_posting_unpaid_legal_product_list(self, api, mock_api_request):
        """Тестирует метод posting_unpaid_legal_product_list."""

        mock_api_request.return_value = {
            "products": [
                {
                    "product_id": 10,
                    "offer_id": "ART-1",
                    "quantity": 2,
                    "name": "Товар",
                    "image_url": "https://example/img.jpg",
                }
            ],
            "cursor": "next",
        }

        request = PostingUnpaidLegalProductListRequest(limit=100)

        response = await api.posting_unpaid_legal_product_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/unpaid-legal/product/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingUnpaidLegalProductListResponse)
        assert response.products[0].product_id == 10
        assert response.cursor == "next"
