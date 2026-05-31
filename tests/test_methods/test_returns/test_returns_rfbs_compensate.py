import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsRfbsCompensateRequest,
    ReturnsRfbsCompensateResponse,
)


class TestReturnsRfbsCompensate:
    """Тесты для метода returns_rfbs_compensate."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_compensate(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_compensate."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsCompensateRequest(return_id=12345, compensation_amount="100")

        response = await api.returns_rfbs_compensate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/compensate",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsCompensateResponse)
