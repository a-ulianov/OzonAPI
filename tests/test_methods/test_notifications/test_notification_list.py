import pytest

from src.ozonapi.seller.schemas.notifications import NotificationListResponse


class TestNotificationList:
    """Тесты для метода notification_list."""

    @pytest.mark.asyncio
    async def test_notification_list(self, api, mock_api_request):
        """Тестирует метод notification_list."""

        mock_api_request.return_value = {
            "urls": [
                {
                    "id": 123,
                    "url": "https://example.com/ozon",
                    "enable": True,
                    "created_at": "2026-06-01T00:00:00Z",
                    "types": [
                        {"type": "TYPE_NEW_POSTING", "description": "Новое отправление"}
                    ],
                }
            ]
        }

        response = await api.notification_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/list",
            payload={}
        )

        assert isinstance(response, NotificationListResponse)
        assert response.urls[0].id == 123
        assert response.urls[0].enable is True
        assert response.urls[0].types[0].type == "TYPE_NEW_POSTING"
