import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSCancelResponse


class TestPostingFBSCancel:
    """Тесты для метода posting_fbs_cancel."""

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel(self, api, mock_api_request):
        """Тестирует метод posting_fbs_cancel."""

        mock_response_data = {
            "result": True
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_cancel import (
            PostingFBSCancelRequest
        )

        request = PostingFBSCancelRequest(
            cancel_reason_id=352,
            cancel_reason_message="Product is out of stock",
            posting_number="33920113-1231-1"
        )

        response = await api.posting_fbs_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSCancelResponse)
        assert response.result is True
