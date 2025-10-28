import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSAwaitingDeliveryResponse


class TestPostingFBSAwaitingDelivery:
    """Тесты для метода posting_fbs_waiting_delivery."""

    @pytest.mark.asyncio
    async def test_posting_fbs_awaiting_delivery(self, api, mock_api_request):
        """Тестирует метод posting_fbs_awaiting_delivery."""

        mock_response_data = {
            "result": True
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_awaiting_delivery import (
            PostingFBSAwaitingDeliveryRequest
        )

        request = PostingFBSAwaitingDeliveryRequest(
            posting_number=["33920143-1195-1", "33920143-1195-2"]
        )

        response = await api.posting_fbs_awaiting_delivery(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/awaiting-delivery",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSAwaitingDeliveryResponse)
        assert response.result is True
