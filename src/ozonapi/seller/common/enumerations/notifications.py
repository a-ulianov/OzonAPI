from enum import Enum


class NotificationType(str, Enum):
    """Тип пуш-уведомления.

    Attributes:
        TYPE_NEW_MESSAGE: новое сообщение в чате
        TYPE_UPDATE_MESSAGE: изменение сообщения в чате
        TYPE_MESSAGE_READ: сообщение прочитано
        TYPE_CHAT_CLOSED: чат закрыт
        TYPE_NEW_POSTING: новое отправление
        TYPE_POSTING_SHIPPED: отправление отгружено
        TYPE_POSTING_CANCELLED: отправление отменено
        TYPE_STATE_CHANGED: изменился статус отправления
        TYPE_DELIVERY_DATE_CHANGED: изменилась дата доставки
        TYPE_CUTOFF_DATE_CHANGED: изменилась дата отгрузки
        TYPE_CREATE_ITEM: создан товар
        TYPE_UPDATE_ITEM: обновлён товар
        TYPE_CREATE_OR_UPDATE_ITEM: создан или обновлён товар
        TYPE_STOCKS_CHANGED: изменились остатки
    """
    TYPE_NEW_MESSAGE = "TYPE_NEW_MESSAGE"
    TYPE_UPDATE_MESSAGE = "TYPE_UPDATE_MESSAGE"
    TYPE_MESSAGE_READ = "TYPE_MESSAGE_READ"
    TYPE_CHAT_CLOSED = "TYPE_CHAT_CLOSED"
    TYPE_NEW_POSTING = "TYPE_NEW_POSTING"
    TYPE_POSTING_SHIPPED = "TYPE_POSTING_SHIPPED"
    TYPE_POSTING_CANCELLED = "TYPE_POSTING_CANCELLED"
    TYPE_STATE_CHANGED = "TYPE_STATE_CHANGED"
    TYPE_DELIVERY_DATE_CHANGED = "TYPE_DELIVERY_DATE_CHANGED"
    TYPE_CUTOFF_DATE_CHANGED = "TYPE_CUTOFF_DATE_CHANGED"
    TYPE_CREATE_ITEM = "TYPE_CREATE_ITEM"
    TYPE_UPDATE_ITEM = "TYPE_UPDATE_ITEM"
    TYPE_CREATE_OR_UPDATE_ITEM = "TYPE_CREATE_OR_UPDATE_ITEM"
    TYPE_STOCKS_CHANGED = "TYPE_STOCKS_CHANGED"
