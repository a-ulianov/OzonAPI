from ...core import APIManager
from ...schemas.chats import (
    ChatListRequest,
    ChatListResponse,
)


class ChatListMixin(APIManager):
    """Реализует метод /v3/chat/list"""

    async def chat_list(
            self: "ChatListMixin",
            request: ChatListRequest
    ) -> ChatListResponse:
        """Возвращает список чатов продавца с покупателями.

        Notes:
            • Курсорная пагинация (`cursor` + `has_next`); фильтр по статусу и
              непрочитанным сообщениям. Каждый элемент содержит вложенный объект `chat`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatListV3

        Args:
            request: Запрос списка чатов по схеме `ChatListRequest`

        Returns:
            Список чатов по схеме `ChatListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_list(ChatListRequest(limit=30))
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="chat/list",
            payload=request.model_dump(by_alias=True)
        )
        return ChatListResponse(**response)
