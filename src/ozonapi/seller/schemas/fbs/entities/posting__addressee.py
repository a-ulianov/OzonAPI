from ...base import BaseAddressee


class PostingFBSAddressee(BaseAddressee):
    """Контактные данные получателя.

    Attributes:
        name (str | None): Имя покупателя
        phone (str | None): Всегда возвращает пустую строку (для получения подменного номера метод posting_fbs_get())
    """
    pass