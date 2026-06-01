import pytest

from src.ozonapi.seller.schemas.postings import (
    PostingCancelRequest,
    PostingCancelResponse,
)


class TestPostingCancel:
    """Тесты для метода posting_cancel."""

    @pytest.mark.asyncio
    async def test_posting_cancel(self, api, mock_api_request):
        """Тестирует метод posting_cancel."""

        mock_api_request.return_value = {"message": "success"}

        request = PostingCancelRequest(
            posting_number="0001-1",
            reason_id=402,
            reason_message="Нет товара на складе",
        )

        response = await api.posting_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/cancel",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingCancelResponse)
        assert response.message == "success"
