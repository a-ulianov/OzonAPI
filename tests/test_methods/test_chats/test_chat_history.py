import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatHistoryRequest,
    ChatHistoryResponse,
)


class TestChatHistory:
    """Тесты для метода chat_history."""

    @pytest.mark.asyncio
    async def test_chat_history(self, api, mock_api_request):
        """Тестирует метод chat_history."""

        mock_api_request.return_value = {
            "has_next": False,
            "messages": [
                {
                    "context": {"order_number": "0001-1", "sku": "123"},
                    "created_at": "2026-04-01T10:05:00Z",
                    "data": ["Здравствуйте!"],
                    "is_image": False,
                    "is_read": True,
                    "message_id": 7,
                    "moderate_image_status": "",
                    "user": {"id": "u-1", "type": "Customer"},
                }
            ],
        }

        request = ChatHistoryRequest(chat_id="chat-1", limit=50)

        response = await api.chat_history(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="chat/history",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ChatHistoryResponse)
        assert response.messages[0].message_id == 7
        assert response.messages[0].user.type == "Customer"
        assert response.messages[0].context.order_number == "0001-1"
