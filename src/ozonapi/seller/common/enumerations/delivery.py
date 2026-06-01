from enum import Enum


class DeliveryMethodStatus(str, Enum):
    """Статус метода доставки.

    Attributes:
        NEW: создан
        EDITED: редактируется
        ACTIVE: активный
        DISABLED: неактивный
    """
    NEW = "NEW"
    EDITED = "EDITED"
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    WAITING = "WAITING"
    BROKEN = "BROKEN"


class SortDir(str, Enum):
    """Направление сортировки.

    Attributes:
        ASC: по возрастанию
        DESC: по убыванию
    """
    ASC = "ASC"
    DESC = "DESC"


class DeliverySchema(str, Enum):
    """Схема доставки для расчёта вариантов.

    Attributes:
        MIX: Смешанная схема
        FBO: Доставка со склада Ozon
        FBS: Доставка со склада продавца
    """
    MIX = "MIX"
    FBO = "FBO"
    FBS = "FBS"
