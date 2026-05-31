import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatListFilter,
    ChatListRequest,
    ChatListResponse,
)


class TestChatList:
    """Тесты для метода chat_list."""

    @pytest.mark.asyncio
    async def test_chat_list(self, api, mock_api_request):
        """Тестирует метод chat_list."""

        mock_api_request.return_value = {
            "chats": [
                {
                    "chat": {
                        "chat_id": "chat-1",
                        "chat_status": "Opened",
                        "chat_type": "Buyer_Seller",
                        "created_at": "2026-04-01T10:00:00Z",
                    },
                    "first_unread_message_id": 5,
                    "last_message_id": 9,
                    "unread_count": 2,
                }
            ],
            "total_unread_count": 2,
            "cursor": "next-cursor",
            "has_next": False,
        }

        request = ChatListRequest(
            filter=ChatListFilter(chat_status="Opened", unread_only=True), limit=30
        )

        response = await api.chat_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="chat/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ChatListResponse)
        assert response.chats[0].chat.chat_id == "chat-1"
        assert response.chats[0].unread_count == 2
        assert response.has_next is False
