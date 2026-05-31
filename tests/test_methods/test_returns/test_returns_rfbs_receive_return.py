import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsRfbsReceiveReturnRequest,
    ReturnsRfbsReceiveReturnResponse,
)


class TestReturnsRfbsReceiveReturn:
    """Тесты для метода returns_rfbs_receive_return."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_receive_return(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_receive_return."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsReceiveReturnRequest(return_id=12345)

        response = await api.returns_rfbs_receive_return(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/receive-return",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsReceiveReturnResponse)
