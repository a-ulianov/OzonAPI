import pytest

from src.ozonapi.seller.schemas.fbs_delivery import PostingFBSSplitRequest, PostingFBSSplitResponse
from src.ozonapi.seller.schemas.fbs_delivery.v1__posting_fbs_split import (
    PostingFBSSplitRequestPosting,
    ProductFbsSplit,
)


class TestPostingFBSSplit:
    """Тесты для метода posting_fbs_split."""

    @pytest.mark.asyncio
    async def test_posting_fbs_split(self, api, mock_api_request):
        """Тестирует метод posting_fbs_split."""

        mock_response_data = {
            "parent_posting": {
                "posting_number": "33920113-1231-1",
                "products": [{"product_id": 123, "quantity": 2}]
            },
            "postings": [
                {
                    "posting_number": "33920113-1231-2",
                    "products": [{"product_id": 123, "quantity": 1}]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSSplitRequest(
            posting_number="33920113-1231-1",
            postings=[
                PostingFBSSplitRequestPosting(products=[ProductFbsSplit(product_id=123, quantity=1)])
            ]
        )

        response = await api.posting_fbs_split(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/split",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSSplitResponse)
        assert response.parent_posting.posting_number == "33920113-1231-1"
        assert response.postings[0].products[0].product_id == 123
