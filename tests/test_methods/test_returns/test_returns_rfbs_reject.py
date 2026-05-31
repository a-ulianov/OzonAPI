import pytest

from src.ozonapi.seller.schemas.returns import ReturnsRfbsRejectRequest, ReturnsRfbsRejectResponse


class TestReturnsRfbsReject:
    """Тесты для метода returns_rfbs_reject."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_reject(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_reject."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsRejectRequest(return_id=12345, rejection_reason_id=1)

        response = await api.returns_rfbs_reject(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/reject",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsRejectResponse)
