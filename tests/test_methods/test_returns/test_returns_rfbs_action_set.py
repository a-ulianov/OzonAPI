import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsRfbsActionSetRequest,
    ReturnsRfbsActionSetResponse,
)


class TestReturnsRfbsActionSet:
    """Тесты для метода returns_rfbs_action_set."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_action_set(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_action_set."""

        mock_api_request.return_value = {}

        request = ReturnsRfbsActionSetRequest(return_id=12345, id=1)

        response = await api.returns_rfbs_action_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/rfbs/action/set",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsActionSetResponse)
