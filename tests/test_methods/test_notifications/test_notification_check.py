import pytest

from src.ozonapi.seller.schemas.notifications import (
    NotificationCheckRequest,
    NotificationCheckResponse,
)


class TestNotificationCheck:
    """Тесты для метода notification_check."""

    @pytest.mark.asyncio
    async def test_notification_check(self, api, mock_api_request):
        """Тестирует метод notification_check."""

        mock_api_request.return_value = {
            "is_active": False,
            "errors": [
                {"type": "REQUEST_TIMEOUT", "description": "Превышено время ожидания"}
            ],
        }

        request = NotificationCheckRequest(url="https://example.com/ozon")

        response = await api.notification_check(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/check",
            payload=request.model_dump()
        )

        assert isinstance(response, NotificationCheckResponse)
        assert response.is_active is False
        assert response.errors[0].type == "REQUEST_TIMEOUT"
