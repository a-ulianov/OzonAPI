import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingFBSListFilter,
    PostingFBSListRequest,
    PostingFBSListResponse,
)


class TestPostingFBSList:
    """Тесты для метода posting_fbs_list (v4)."""

    @pytest.mark.asyncio
    async def test_posting_fbs_list(self, api, mock_api_request):
        """Тестирует метод posting_fbs_list."""

        mock_api_request.return_value = {
            "cursor": "next",
            "has_next": True,
            "postings": [{"posting_number": "123-456-1", "status": "awaiting_packaging"}],
        }

        request = PostingFBSListRequest(
            filter=PostingFBSListFilter(
                since="2026-05-01T00:00:00Z", to="2026-06-01T00:00:00Z"
            ),
            limit=100,
        )

        response = await api.posting_fbs_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSListResponse)
        assert response.has_next is True
        assert response.postings[0].posting_number == "123-456-1"
