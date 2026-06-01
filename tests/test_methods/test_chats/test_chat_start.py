import pytest

from src.ozonapi.seller.schemas.chats import (
    ChatStartRequest,
    ChatStartResponse,
)


class TestChatStart:
    """Тесты для метода chat_start."""

    @pytest.mark.asyncio
    async def test_chat_start(self, api, mock_api_request):
        """Тестирует метод chat_start."""

        mock_api_request.return_value = {"result": {"chat_id": "chat-123"}}

        request = ChatStartRequest(posting_number="0001-1234567-0000001")

        response = await api.chat_start(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="chat/start",
            payload=request.model_dump(),
        )

        assert isinstance(response, ChatStartResponse)
        assert response.result.chat_id == "chat-123"
