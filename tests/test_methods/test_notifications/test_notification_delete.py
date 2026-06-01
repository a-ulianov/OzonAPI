import pytest

from src.ozonapi.seller.schemas.notifications import (
    NotificationDeleteRequest,
    NotificationDeleteResponse,
)


class TestNotificationDelete:
    """Тесты для метода notification_delete."""

    @pytest.mark.asyncio
    async def test_notification_delete(self, api, mock_api_request):
        """Тестирует метод notification_delete."""

        mock_api_request.return_value = {}

        request = NotificationDeleteRequest(id=123)

        response = await api.notification_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, NotificationDeleteResponse)
