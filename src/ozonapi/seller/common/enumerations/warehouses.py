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