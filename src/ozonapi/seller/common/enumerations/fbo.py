from enum import Enum


class ItemSortField(str, Enum):
    """Поле сортировки товаров в составе поставки.

    Attributes:
        SKU: по идентификатору товара в системе Ozon (SKU)
        NAME: по названию товара
        QUANTITY: по количеству товара
        TOTAL_VOLUME_IN_LITRES: по суммарному объёму товаров в литрах
    """
    SKU = "SKU"
    NAME = "NAME"
    QUANTITY = "QUANTITY"
    TOTAL_VOLUME_IN_LITRES = "TOTAL_VOLUME_IN_LITRES"


class SupplyOrderState(str, Enum):
    """Статус заявки на поставку (для фильтрации в `supply_order_list`).

    Attributes:
        DATA_FILLING: заполнение данных
        READY_TO_SUPPLY: готова к отгрузке
        ACCEPTED_AT_SUPPLY_WAREHOUSE: принята в пункте отгрузки
        IN_TRANSIT: в пути
        ACCEPTANCE_AT_STORAGE_WAREHOUSE: приёмка на складе хранения
        REPORTS_CONFIRMATION_AWAITING: ожидает подтверждения отчётов
        REPORT_REJECTED: отчёт отклонён
        COMPLETED: завершена
        REJECTED_AT_SUPPLY_WAREHOUSE: отклонена в пункте отгрузки
        CANCELLED: отменена
        OVERDUE: просрочена
    """
    DATA_FILLING = "DATA_FILLING"
    READY_TO_SUPPLY = "READY_TO_SUPPLY"
    ACCEPTED_AT_SUPPLY_WAREHOUSE = "ACCEPTED_AT_SUPPLY_WAREHOUSE"
    IN_TRANSIT = "IN_TRANSIT"
    ACCEPTANCE_AT_STORAGE_WAREHOUSE = "ACCEPTANCE_AT_STORAGE_WAREHOUSE"
    REPORTS_CONFIRMATION_AWAITING = "REPORTS_CONFIRMATION_AWAITING"
    REPORT_REJECTED = "REPORT_REJECTED"
    COMPLETED = "COMPLETED"
    REJECTED_AT_SUPPLY_WAREHOUSE = "REJECTED_AT_SUPPLY_WAREHOUSE"
    CANCELLED = "CANCELLED"
    OVERDUE = "OVERDUE"


class SupplyOrderSortField(str, Enum):
    """Поле сортировки списка заявок на поставку.

    Attributes:
        ORDER_CREATION: по дате создания заявки
        ORDER_STATE_UPDATED_AT: по дате обновления статуса заявки
        TIMESLOT_FROM_UTC: по началу интервала поставки (UTC)
        TIMESLOT_FROM_LOCAL: по началу интервала поставки (местное время)
    """
    ORDER_CREATION = "ORDER_CREATION"
    ORDER_STATE_UPDATED_AT = "ORDER_STATE_UPDATED_AT"
    TIMESLOT_FROM_UTC = "TIMESLOT_FROM_UTC"
    TIMESLOT_FROM_LOCAL = "TIMESLOT_FROM_LOCAL"


class SupplyOrderSortDirection(str, Enum):
    """Направление сортировки списка заявок на поставку.

    Attributes:
        ASC: по возрастанию
        DESC: по убыванию
    """
    ASC = "ASC"
    DESC = "DESC"


class TimeslotFilterType(str, Enum):
    """Тип фильтрации интервалов поставки по времени.

    Attributes:
        BY_LOCAL_TIME: по местному времени
        BY_UTC_TIME: по времени UTC
    """
    BY_LOCAL_TIME = "BY_LOCAL_TIME"
    BY_UTC_TIME = "BY_UTC_TIME"
