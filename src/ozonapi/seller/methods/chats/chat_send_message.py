from ...core import APIManager
from ...schemas.chats import (
    ChatSendMessageRequest,
    ChatSendMessageResponse,
)


class ChatSendMessageMixin(APIManager):
    """Реализует метод /v1/chat/send/message"""

    async def chat_send_message(
            self: "ChatSendMessageMixin",
            request: ChatSendMessageRequest,
    ) -> ChatSendMessageResponse:
        """Отправляет текстовое сообщение в чат с покупателем (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Метод изменяет данные (отправляет сообщение).

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatSendMessage

        Args:
            request: Запрос отправки сообщения по схеме `ChatSendMessageRequest`

        Returns:
            Результат отправки по схеме `ChatSendMessageResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_send_message(
                    ChatSendMessageRequest(chat_id="abc", text="Здравствуйте!")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="chat/send/message",
            payload=request.model_dump(),
        )
        return ChatSendMessageResponse(**response)
