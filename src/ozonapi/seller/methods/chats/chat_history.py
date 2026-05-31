from ...core import APIManager
from ...schemas.chats import (
    ChatHistoryRequest,
    ChatHistoryResponse,
)


class ChatHistoryMixin(APIManager):
    """Реализует метод /v3/chat/history"""

    async def chat_history(
            self: "ChatHistoryMixin",
            request: ChatHistoryRequest
    ) -> ChatHistoryResponse:
        """Возвращает историю сообщений чата.

        Notes:
            • Сообщения сортируются по дате создания; направление задаётся `direction`
              (`Forward`/`Backward`), стартовая точка — `from_message_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatHistoryV3

        Args:
            request: Запрос истории чата по схеме `ChatHistoryRequest`

        Returns:
            История чата по схеме `ChatHistoryResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_history(
                    ChatHistoryRequest(chat_id="abc", limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="chat/history",
            payload=request.model_dump(by_alias=True)
        )
        return ChatHistoryResponse(**response)
