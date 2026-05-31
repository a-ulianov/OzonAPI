import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSDigitalActCheckStatusRequest,
    PostingFBSDigitalActCheckStatusResponse,
)


class TestPostingFBSDigitalActCheckStatus:
    """Тесты для метода posting_fbs_digital_act_check_status."""

    @pytest.mark.asyncio
    async def test_posting_fbs_digital_act_check_status(self, api, mock_api_request):
        """Тестирует метод posting_fbs_digital_act_check_status."""

        mock_response_data = {"id": 12345, "status": "FORMED"}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSDigitalActCheckStatusRequest(id=12345)

        response = await api.posting_fbs_digital_act_check_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/digital/act/check-status",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSDigitalActCheckStatusResponse)
        assert response.id == 12345
        assert response.status == "FORMED"
