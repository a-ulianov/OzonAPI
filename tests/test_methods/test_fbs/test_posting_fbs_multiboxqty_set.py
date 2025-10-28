import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSMultiBoxQtySetResponse


class TestPostingFBSMultiBoxQty(object):
    """Тесты для метода posting_fbs_multiboxqty_set."""

    @pytest.mark.asyncio
    async def test_posting_fbs_multiboxqty_set(self, api, mock_api_request):
        """Тестирует метод posting_fbs_multiboxqty_set."""

        mock_response_data = {
            "result": {
                "result": True
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v3__posting_multiboxqty_set import (
            PostingFBSMultiBoxQtySetRequest
        )

        request = PostingFBSMultiBoxQtySetRequest(
            posting_number="57195475-0050-3",
            multi_box_qty=3
        )

        response = await api.posting_fbs_multiboxqty_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/multi-box-qty/set",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSMultiBoxQtySetResponse)
        assert response.result.result is True
