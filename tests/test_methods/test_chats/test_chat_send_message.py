import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatSendMessageRequest,
    ChatSendMessageResponse,
)


class TestChatSendMessage:
    """Тесты для метода chat_send_message."""

    @pytest.mark.asyncio
    async def test_chat_send_message(self, api, mock_api_request):
        """Тестирует метод chat_send_message."""

        mock_api_request.return_value = {"result": "success"}

        request = ChatSendMessageRequest(chat_id="abc", text="Здравствуйте!")

        response = await api.chat_send_message(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="chat/send/message",
            payload=request.model_dump(),
        )

        assert isinstance(response, ChatSendMessageResponse)
        assert response.result == "success"
