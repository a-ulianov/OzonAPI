from ...core import APIManager
from ...schemas.chats import (
    ChatSendFileRequest,
    ChatSendFileResponse,
)


class ChatSendFileMixin(APIManager):
    """Реализует метод /v1/chat/send/file"""

    async def chat_send_file(
            self: "ChatSendFileMixin",
            request: ChatSendFileRequest
    ) -> ChatSendFileResponse:
        """Отправляет файл в чат с покупателем.

        Notes:
            • Файл передаётся строкой base64 в поле `base64_content`; `name` должно
              содержать расширение. Метод изменяет данные (отправляет сообщение).

        References:
            https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatSendFile

        Args:
            request: Запрос отправки файла по схеме `ChatSendFileRequest`

        Returns:
            Результат отправки по схеме `ChatSendFileResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.chat_send_file(
                    ChatSendFileRequest(
                        chat_id="abc", base64_content="...", name="doc.pdf"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="chat/send/file",
            payload=request.model_dump(by_alias=True)
        )
        return ChatSendFileResponse(**response)
