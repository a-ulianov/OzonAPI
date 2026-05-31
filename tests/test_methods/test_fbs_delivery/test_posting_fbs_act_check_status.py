import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSActCheckStatusRequest,
    PostingFBSActCheckStatusResponse,
)


class TestPostingFBSActCheckStatus:
    """Тесты для метода posting_fbs_act_check_status."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_check_status(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_check_status."""

        mock_response_data = {
            "result": {
                "act_type": "act_type_default",
                "added_to_act": ["33920113-1231-1"],
                "removed_from_act": [],
                "status": "ready",
                "is_partial": False,
                "partial_num": 0
            }
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActCheckStatusRequest(id=12345)

        response = await api.posting_fbs_act_check_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/check-status",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSActCheckStatusResponse)
        assert response.result.status == "ready"
        assert response.result.added_to_act == ["33920113-1231-1"]
