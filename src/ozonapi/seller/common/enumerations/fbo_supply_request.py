from enum import Enum


class SupplyClusterType(str, Enum):
    """Тип кластера для поиска при создании заявки на поставку FBO.

    Attributes:
        OZON: Кластеры Ozon
        CIS: Кластеры СНГ
    """
    OZON = "CLUSTER_TYPE_OZON"
    CIS = "CLUSTER_TYPE_CIS"


class SupplyCreateType(str, Enum):
    """Тип поставки при поиске точек отгрузки FBO.

    Attributes:
        CROSSDOCK: Поставка кросс-докингом
        DIRECT: Прямая поставка
    """
    CROSSDOCK = "CREATE_TYPE_CROSSDOCK"
    DIRECT = "CREATE_TYPE_DIRECT"


class SupplyType(str, Enum):
    """Тип поставки заявки на поставку FBO.

    Attributes:
        CROSSDOCK: Поставка кросс-докингом
        DIRECT: Прямая поставка
        MULTI_CLUSTER: Поставка для нескольких кластеров
    """
    CROSSDOCK = "CROSSDOCK"
    DIRECT = "DIRECT"
    MULTI_CLUSTER = "MULTI_CLUSTER"


class SupplyDeleteSkuMode(str, Enum):
    """Режим удаления товаров при создании черновика заявки на поставку.

    Attributes:
        PARTIAL: Частичное удаление недоступных товаров
        FULL: Полное удаление при наличии недоступных товаров
    """
    PARTIAL = "PARTIAL"
    FULL = "FULL"


class SupplyDeliveryType(str, Enum):
    """Тип доставки до точки отгрузки в заявке на поставку.

    Attributes:
        DROPOFF: Отгрузка в пункте приёма
        PICKUP: Забор от продавца
    """
    DROPOFF = "DROPOFF"
    PICKUP = "PICKUP"


class SupplyDropOffWarehouseType(str, Enum):
    """Тип точки отгрузки в заявке на поставку.

    Attributes:
        DELIVERY_POINT: Пункт выдачи
        SORTING_CENTER: Сортировочный центр
        CROSS_DOCK: Транзитный склад
        ORDERS_RECEIVING_POINT: Пункт приёма заказов
        FULL_FILLMENT: Склад с полным циклом обработки
    """
    DELIVERY_POINT = "DELIVERY_POINT"
    SORTING_CENTER = "SORTING_CENTER"
    CROSS_DOCK = "CROSS_DOCK"
    ORDERS_RECEIVING_POINT = "ORDERS_RECEIVING_POINT"
    FULL_FILLMENT = "FULL_FILLMENT"
