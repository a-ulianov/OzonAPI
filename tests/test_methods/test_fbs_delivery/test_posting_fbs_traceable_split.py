import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSTraceableSplitRequest,
    PostingFBSTraceableSplitResponse,
)


class TestPostingFBSTraceableSplit:
    """Тесты для метода posting_fbs_traceable_split."""

    @pytest.mark.asyncio
    async def test_posting_fbs_traceable_split(self, api, mock_api_request):
        """Тестирует метод posting_fbs_traceable_split."""

        mock_response_data = {
            "postings": [
                {
                    "posting_number": "33920113-1231-2",
                    "potential_blr_traceable": True,
                    "products": [{"sku": 987654, "quantity": 1}]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSTraceableSplitRequest(posting_number="33920113-1231-1")

        response = await api.posting_fbs_traceable_split(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/traceable/split",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSTraceableSplitResponse)
        assert response.postings[0].potential_blr_traceable is True
        assert response.postings[0].products[0].sku == 987654
