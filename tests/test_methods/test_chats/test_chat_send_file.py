import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatSendFileRequest,
    ChatSendFileResponse,
)


class TestChatSendFile:
    """Тесты для метода chat_send_file."""

    @pytest.mark.asyncio
    async def test_chat_send_file(self, api, mock_api_request):
        """Тестирует метод chat_send_file."""

        mock_api_request.return_value = {"result": "success"}

        request = ChatSendFileRequest(
            chat_id="chat-1", base64_content="ZmlsZQ==", name="doc.pdf"
        )

        response = await api.chat_send_file(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="chat/send/file",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ChatSendFileResponse)
        assert response.result == "success"
