from ...core import APIManager
from ...schemas.chats import (
    ChatReadRequest,
    ChatReadResponse,
)


class ChatReadMixin(APIManager):
    """Реализует метод /v2/chat/read"""

    async def chat_read(
            self: "ChatReadMixin",
            request: ChatReadRequest,
    ) -> ChatReadResponse:
        """Отмечает сообщения чата как прочитанные (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Сообщения отмечаются прочитанными, начиная с `from_message_id`.
            • В ответе возвращается остаток непрочитанных сообщений.

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatReadV2

        Args:
            request: Запрос отметки сообщений по схеме `ChatReadRequest`

        Returns:
            Количество непрочитанных сообщений по схеме `ChatReadResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_read(
                    ChatReadRequest(chat_id="abc", from_message_id=123456)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="chat/read",
            payload=request.model_dump(),
        )
        return ChatReadResponse(**response)
