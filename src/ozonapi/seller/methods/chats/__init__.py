"""Композиция миксинов методов раздела Чаты с покупателями.

Объединяет методы работы с чатами в единый класс :class:`SellerChatAPI`.
"""

from ...core import APIManager
from .chat_history import ChatHistoryMixin
from .chat_list import ChatListMixin
from .chat_list_v2 import ChatListV2Mixin
from .chat_send_file import ChatSendFileMixin


class SellerChatAPI(
    ChatHistoryMixin,
    ChatListMixin,
    ChatListV2Mixin,
    ChatSendFileMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Чаты с покупателями.

    Notes:
        • Объединяет методы списка чатов (v2/v3), истории чата и отправки файла.

    References:
        • https://docs.ozon.ru/api/seller/#tag/ChatAPI
    """

    pass
