import pytest

from src.ozonapi.seller.schemas.notifications import NotificationPushTypeListResponse


class TestNotificationPushTypeList:
    """Тесты для метода notification_push_type_list."""

    @pytest.mark.asyncio
    async def test_notification_push_type_list(self, api, mock_api_request):
        """Тестирует метод notification_push_type_list."""

        mock_api_request.return_value = {
            "types": [
                {
                    "type": "TYPE_NEW_POSTING",
                    "description": "Новое отправление",
                    "seller_endpoint": {"id": 123, "url": "https://example.com/ozon"},
                }
            ]
        }

        response = await api.notification_push_type_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="notification/push-type/list",
            payload={}
        )

        assert isinstance(response, NotificationPushTypeListResponse)
        assert response.types[0].type == "TYPE_NEW_POSTING"
        assert response.types[0].seller_endpoint.id == 123
