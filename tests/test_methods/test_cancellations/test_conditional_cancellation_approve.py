import pytest

from src.ozonapi.seller.schemas.cancellations import (
    ConditionalCancellationApproveRequest,
    ConditionalCancellationApproveResponse,
)


class TestConditionalCancellationApprove:
    """Тесты для метода conditional_cancellation_approve."""

    @pytest.mark.asyncio
    async def test_conditional_cancellation_approve(self, api, mock_api_request):
        """Тестирует метод conditional_cancellation_approve."""

        mock_api_request.return_value = {}

        request = ConditionalCancellationApproveRequest(
            cancellation_id=123, comment="ок"
        )

        response = await api.conditional_cancellation_approve(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/approve",
            payload=request.model_dump()
        )

        assert isinstance(response, ConditionalCancellationApproveResponse)
