from ...core import APIManager
from ...schemas.chats import (
    ChatStartRequest,
    ChatStartResponse,
)


class ChatStartMixin(APIManager):
    """Реализует метод /v1/chat/start"""

    async def chat_start(
            self: "ChatStartMixin",
            request: ChatStartRequest,
    ) -> ChatStartResponse:
        """Создаёт новый чат с покупателем по отправлению (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • В ответе возвращается идентификатор созданного чата.

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatStart

        Args:
            request: Запрос создания чата по схеме `ChatStartRequest`

        Returns:
            Идентификатор созданного чата по схеме `ChatStartResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_start(
                    ChatStartRequest(posting_number="0001-1234567-0000001")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="chat/start",
            payload=request.model_dump(),
        )
        return ChatStartResponse(**response)
