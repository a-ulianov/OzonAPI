"""Схемы раздела Чаты с покупателями."""
__all__ = [
    "ChatListRequest",
    "ChatListDetails",
    "ChatListItem",
    "ChatListResponse",
    "ChatListV2Request",
    "ChatListV2Item",
    "ChatListV2Response",
    "ChatHistoryRequest",
    "ChatHistoryRequestFilter",
    "ChatMessage",
    "ChatMessageContext",
    "ChatMessageUser",
    "ChatHistoryResponse",
    "ChatSendFileRequest",
    "ChatSendFileResponse",
    "ChatListFilter",
]

from .entities import ChatListFilter
from .v1__chat_send_file import (
    ChatSendFileRequest,
    ChatSendFileResponse,
)
from .v2__chat_list import (
    ChatListV2Item,
    ChatListV2Request,
    ChatListV2Response,
)
from .v3__chat_history import (
    ChatHistoryRequest,
    ChatHistoryRequestFilter,
    ChatHistoryResponse,
    ChatMessage,
    ChatMessageContext,
    ChatMessageUser,
)
from .v3__chat_list import (
    ChatListDetails,
    ChatListItem,
    ChatListRequest,
    ChatListResponse,
)
