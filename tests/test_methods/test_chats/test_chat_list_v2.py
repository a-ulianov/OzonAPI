import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatListV2Request,
    ChatListV2Response,
)


class TestChatListV2:
    """Тесты для метода chat_list_v2."""

    @pytest.mark.asyncio
    async def test_chat_list_v2(self, api, mock_api_request):
        """Тестирует метод chat_list_v2."""

        mock_api_request.return_value = {
            "chats": [
                {
                    "chat_id": "chat-2",
                    "chat_status": "Closed",
                    "chat_type": "Seller_Support",
                    "created_at": "2026-04-02T10:00:00Z",
                    "first_unread_message_id": 0,
                    "last_message_id": 3,
                    "unread_count": 0,
                }
            ],
            "total_chats_count": 1,
            "total_unread_count": 0,
        }

        request = ChatListV2Request(limit=30, offset=0)

        response = await api.chat_list_v2(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="chat/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ChatListV2Response)
        assert response.chats[0].chat_id == "chat-2"
        assert response.total_chats_count == 1
