import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSActGetPostingsRequest,
    PostingFBSActGetPostingsResponse,
)


class TestPostingFBSActGetPostings:
    """Тесты для метода posting_fbs_act_get_postings."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_get_postings(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_get_postings."""

        mock_response_data = {
            "result": [
                {
                    "id": 12345,
                    "posting_number": "33920113-1231-1",
                    "status": "delivering",
                    "multi_box_qty": 1,
                    "products": [
                        {"name": "Товар", "offer_id": "ART-1", "price": "199.00", "quantity": 2, "sku": 987654}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActGetPostingsRequest(id=12345)

        response = await api.posting_fbs_act_get_postings(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-postings",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSActGetPostingsResponse)
        assert response.result[0].posting_number == "33920113-1231-1"
        assert response.result[0].products[0].sku == 987654
