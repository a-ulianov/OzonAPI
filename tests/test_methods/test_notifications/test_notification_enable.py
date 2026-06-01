import pytest

from src.ozonapi.seller.schemas.notifications import (
    NotificationEnableRequest,
    NotificationEnableResponse,
)


class TestNotificationEnable:
    """Тесты для метода notification_enable."""

    @pytest.mark.asyncio
    async def test_notification_enable(self, api, mock_api_request):
        """Тестирует метод notification_enable."""

        mock_api_request.return_value = {}

        request = NotificationEnableRequest(id=123, enabled=True)

        response = await api.notification_enable(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/enable",
            payload=request.model_dump()
        )

        assert isinstance(response, NotificationEnableResponse)
