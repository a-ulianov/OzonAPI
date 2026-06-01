import pytest

from src.ozonapi.seller.schemas.cancellations import (
    ConditionalCancellationRejectRequest,
    ConditionalCancellationRejectResponse,
)


class TestConditionalCancellationReject:
    """Тесты для метода conditional_cancellation_reject."""

    @pytest.mark.asyncio
    async def test_conditional_cancellation_reject(self, api, mock_api_request):
        """Тестирует метод conditional_cancellation_reject."""

        mock_api_request.return_value = {}

        request = ConditionalCancellationRejectRequest(
            cancellation_id=123, comment="передано в доставку"
        )

        response = await api.conditional_cancellation_reject(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/reject",
            payload=request.model_dump()
        )

        assert isinstance(response, ConditionalCancellationRejectResponse)
