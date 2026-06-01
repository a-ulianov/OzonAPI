import pytest

from src.ozonapi.seller.schemas.notifications import (
    NotificationUpdateRequest,
    NotificationUpdateResponse,
)


class TestNotificationUpdate:
    """Тесты для метода notification_update."""

    @pytest.mark.asyncio
    async def test_notification_update(self, api, mock_api_request):
        """Тестирует метод notification_update."""

        mock_api_request.return_value = {}

        request = NotificationUpdateRequest(
            id=123,
            url="https://example.com/ozon",
            types=["TYPE_NEW_POSTING"],
        )

        response = await api.notification_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/update",
            payload=request.model_dump()
        )

        assert isinstance(response, NotificationUpdateResponse)
