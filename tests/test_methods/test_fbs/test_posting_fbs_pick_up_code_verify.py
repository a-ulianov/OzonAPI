import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingFBSPickUpCodeVerifyRequest,
    PostingFBSPickUpCodeVerifyResponse,
)


class TestPostingFBSPickUpCodeVerify:
    """Тесты для метода posting_fbs_pick_up_code_verify."""

    @pytest.mark.asyncio
    async def test_posting_fbs_pick_up_code_verify(self, api, mock_api_request):
        """Тестирует метод posting_fbs_pick_up_code_verify."""

        mock_api_request.return_value = {"valid": True}

        request = PostingFBSPickUpCodeVerifyRequest(
            posting_number="123-456-1", pickup_code="0000"
        )

        response = await api.posting_fbs_pick_up_code_verify(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/pick-up-code/verify",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSPickUpCodeVerifyResponse)
        assert response.valid is True
