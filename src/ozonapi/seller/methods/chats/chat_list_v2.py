from ...core import APIManager
from ...schemas.chats import (
    ChatListV2Request,
    ChatListV2Response,
)


class ChatListV2Mixin(APIManager):
    """Реализует метод /v2/chat/list"""

    async def chat_list_v2(
            self: "ChatListV2Mixin",
            request: ChatListV2Request
    ) -> ChatListV2Response:
        """Возвращает список чатов продавца (устаревшая версия 2).

        Notes:
            • Постраничная выдача через `limit`/`offset`. Элементы чатов плоские
              (без вложенного объекта `chat`).
            • УСТАРЕЛ И УДАЛЁН ИЗ СПЕЦИФИКАЦИИ: с 2026-06-10 операция
              `/v2/chat/list` исключена из OpenAPI-спецификации Ozon Seller API;
              на стороне Ozon endpoint возвращает 404. Используйте `chat_list()`
              (v3). Метод сохранён в библиотеке для обратной совместимости и будет
              удалён в одном из будущих мажорных релизов.

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatListV2

        Args:
            request: Запрос списка чатов по схеме `ChatListV2Request`

        Returns:
            Список чатов по схеме `ChatListV2Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_list_v2(ChatListV2Request(limit=30, offset=0))
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="chat/list",
            payload=request.model_dump(by_alias=True)
        )
        return ChatListV2Response(**response)
