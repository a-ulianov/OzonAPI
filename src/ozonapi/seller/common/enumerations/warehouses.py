from enum import Enum


class FirstMileType(str, Enum):
    """Тип первой мили.

    Attributes:
        DROPOFF: Выдача
        PICKUP: Забор
        UNSPECIFIED: Не указано
    """
    DROPOFF = "DropOff"
    PICKUP = "Pickup"
    UNSPECIFIED = ""


class WarehouseStatus(str, Enum):
    """Соответствие статусов склада со статусами в личном кабинете.

    Attributes:
        NEW: Новый
        CREATED: Создан
        DISABLED: Отключен
        BLOCKED: Заблокирован
        DISABLED_DUE_TO_LIMIT: Отключен из-за лимита
        ERROR: Ошибка
    """
    NEW = "new"
    CREATED = "created"
    DISABLED = "disabled"
    BLOCKED = "blocked"
    DISABLED_DUE_TO_LIMIT = "disabled_due_to_limit"
    ERROR = "error"


class WarehouseType(str, Enum):
    """Тип склада.

    Attributes:
        FBS: склад продавца, доставка силами Ozon
        RFBS: склад продавца, доставка силами продавца
        FBO: склад Ozon
        FBP: склад партнёра
    """
    FBS = "fbs"
    RFBS = "rfbs"
    FBO = "fbo"
    FBP = "fbp"


class WarehouseWorkingDays(int, Enum):
    """Рабочие дни склада.

    Attributes:
        MONDAY: Понедельник
        TUESDAY: Вторник
        WEDNESDAY: Среда
        THURSDAY: Четверг
        FRIDAY: Пятница
        SATURDAY: Суббота
        SUNDAY: Воскресенье
    """
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class CarriageLabelType(str, Enum):
    """Размер этикетки отгрузки (API v2).

    Attributes:
        UNSPECIFIED: Не указан
        BIG: Большая
        SMALL: Маленькая
    """
    UNSPECIFIED = "UNSPECIFIED"
    BIG = "BIG"
    SMALL = "SMALL"


class FirstMileTypeV2(str, Enum):
    """Тип первой мили склада (API v2).

    Attributes:
        UNSPECIFIED: Не указан
        PICK_UP: Забор
        DROP_OFF: Выдача
    """
    UNSPECIFIED = "UNSPECIFIED"
    PICK_UP = "PICK_UP"
    DROP_OFF = "DROP_OFF"


class WarehouseWorkingDayV2(str, Enum):
    """Рабочий день склада (API v2, строковое представление).

    Attributes:
        UNSPECIFIED: Не указан
        MONDAY: Понедельник
        TUESDAY: Вторник
        WEDNESDAY: Среда
        THURSDAY: Четверг
        FRIDAY: Пятница
        SATURDAY: Суббота
        SUNDAY: Воскресенье
    """
    UNSPECIFIED = "UNSPECIFIED"
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"