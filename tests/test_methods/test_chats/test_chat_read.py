import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatReadRequest,
    ChatReadResponse,
)


class TestChatRead:
    """Тесты для метода chat_read."""

    @pytest.mark.asyncio
    async def test_chat_read(self, api, mock_api_request):
        """Тестирует метод chat_read."""

        mock_api_request.return_value = {"unread_count": 0}

        request = ChatReadRequest(chat_id="abc", from_message_id=123456)

        response = await api.chat_read(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="chat/read",
            payload=request.model_dump(),
        )

        assert isinstance(response, ChatReadResponse)
        assert response.unread_count == 0
