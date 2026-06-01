import pytest

from src.ozonapi.seller.schemas.postings import (
    PostingCancelStatusRequest,
    PostingCancelStatusResponse,
)


class TestPostingCancelStatus:
    """Тесты для метода posting_cancel_status."""

    @pytest.mark.asyncio
    async def test_posting_cancel_status(self, api, mock_api_request):
        """Тестирует метод posting_cancel_status."""

        mock_api_request.return_value = {
            "order_number": "0001",
            "posting_number": ["0001-1", "0001-2"],
            "state": "SUCCESS",
        }

        request = PostingCancelStatusRequest(posting_number="0001-1")

        response = await api.posting_cancel_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/cancel/status",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingCancelStatusResponse)
        assert response.order_number == "0001"
        assert response.posting_number == ["0001-1", "0001-2"]
        assert response.state == "SUCCESS"
