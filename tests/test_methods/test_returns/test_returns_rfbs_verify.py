import pytest

from src.ozonapi.seller.schemas.returns import ReturnsRfbsVerifyRequest, ReturnsRfbsVerifyResponse


class TestReturnsRfbsVerify:
    """Тесты для метода returns_rfbs_verify."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_verify(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_verify."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsVerifyRequest(return_id=12345)

        response = await api.returns_rfbs_verify(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/verify",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsVerifyResponse)
