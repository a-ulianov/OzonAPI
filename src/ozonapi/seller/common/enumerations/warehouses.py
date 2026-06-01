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


class WarehouseFBSPointType(str, Enum):
    """Тип пункта drop-off или возврата при создании склада FBS.

    Attributes:
        PVZ: Пункт выдачи заказов
        PPZ: Пункт приёма заказов
        SC: Сортировочный центр
    """
    PVZ = "PVZ"
    PPZ = "PPZ"
    SC = "SC"


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


class WarehouseOZONType(str, Enum):
    """Тип склада Ozon (фильтр запроса списка складов Ozon).

    Attributes:
        FULL_FILLMENT: Склад фулфилмента
        FULL_FILLMENT_RETURNS: Склад возвратов фулфилмента
        FULL_FILLMENT_DEFECT: Склад брака фулфилмента
        EXPRESS_DARK_STORE: Дарксфор Express
        CROSS_DOCK: Кросс-докинг
        SORTING_CENTER: Сортировочный центр
        PHARMACY: Аптечный склад
        DISTRIBUTION_CENTER: Распределительный центр
        ORDERS_RECEIVING_POINT: Пункт приёма заказов
        OUTSOURCE_FF: Внешний фулфилмент
        B2B: Склад B2B
        EXTERNAL_FF: Внешний фулфилмент-партнёр
    """
    FULL_FILLMENT = "FULL_FILLMENT"
    FULL_FILLMENT_RETURNS = "FULL_FILLMENT_RETURNS"
    FULL_FILLMENT_DEFECT = "FULL_FILLMENT_DEFECT"
    EXPRESS_DARK_STORE = "EXPRESS_DARK_STORE"
    CROSS_DOCK = "CROSS_DOCK"
    SORTING_CENTER = "SORTING_CENTER"
    PHARMACY = "PHARMACY"
    DISTRIBUTION_CENTER = "DISTRIBUTION_CENTER"
    ORDERS_RECEIVING_POINT = "ORDERS_RECEIVING_POINT"
    OUTSOURCE_FF = "OUTSOURCE_FF"
    B2B = "B2B"
    EXTERNAL_FF = "EXTERNAL_FF"


class WarehouseERFBSReturnMethod(str, Enum):
    """Способ возврата для склада rFBS Express.

    Attributes:
        UNSPECIFIED: Не указан
        COURIER: Курьером
        TRANSPORT_COMPANY: Транспортной компанией
    """
    UNSPECIFIED = "UNSPECIFIED"
    COURIER = "COURIER"
    TRANSPORT_COMPANY = "TRANSPORT_COMPANY"
