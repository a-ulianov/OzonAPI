import pytest

from src.ozonapi.seller.schemas.notifications import (
    NotificationSetRequest,
    NotificationSetResponse,
)


class TestNotificationSet:
    """Тесты для метода notification_set."""

    @pytest.mark.asyncio
    async def test_notification_set(self, api, mock_api_request):
        """Тестирует метод notification_set."""

        mock_api_request.return_value = {}

        request = NotificationSetRequest(
            url="https://example.com/ozon",
            types=["TYPE_NEW_POSTING", "TYPE_STATE_CHANGED"],
        )

        response = await api.notification_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/set",
            payload=request.model_dump()
        )

        assert isinstance(response, NotificationSetResponse)
