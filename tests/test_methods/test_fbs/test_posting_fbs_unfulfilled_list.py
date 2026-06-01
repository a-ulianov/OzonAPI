import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingFBSUnfulfilledListFilter,
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse,
)


class TestPostingFBSUnfulfilledList:
    """Тесты для метода posting_fbs_unfulfilled_list (v4)."""

    @pytest.mark.asyncio
    async def test_posting_fbs_unfulfilled_list(self, api, mock_api_request):
        """Тестирует метод posting_fbs_unfulfilled_list."""

        mock_api_request.return_value = {
            "count": 1,
            "cursor": "next",
            "has_next": False,
            "postings": [{"posting_number": "123-456-1", "status": "awaiting_packaging"}],
        }

        request = PostingFBSUnfulfilledListRequest(
            filter=PostingFBSUnfulfilledListFilter(statuses=["awaiting_packaging"]),
            limit=100,
        )

        response = await api.posting_fbs_unfulfilled_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/unfulfilled/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSUnfulfilledListResponse)
        assert response.count == 1
        assert response.postings[0].posting_number == "123-456-1"
