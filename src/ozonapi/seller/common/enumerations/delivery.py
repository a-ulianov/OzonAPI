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