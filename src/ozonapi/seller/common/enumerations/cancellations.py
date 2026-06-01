from enum import Enum


class CancellationInitiator(str, Enum):
    """Инициатор отмены заявки rFBS.

    Attributes:
        OZON: Ozon
        SELLER: Продавец
        CLIENT: Покупатель
        SYSTEM: Система
        DELIVERY: Служба доставки
    """
    OZON = "OZON"
    SELLER = "SELLER"
    CLIENT = "CLIENT"
    SYSTEM = "SYSTEM"
    DELIVERY = "DELIVERY"


class CancellationStateFilter(str, Enum):
    """Фильтр по статусу заявки на отмену rFBS.

    Attributes:
        ALL: Все заявки
        ON_APPROVAL: На рассмотрении
        APPROVED: Подтверждена
        REJECTED: Отклонена
    """
    ALL = "ALL"
    ON_APPROVAL = "ON_APPROVAL"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
