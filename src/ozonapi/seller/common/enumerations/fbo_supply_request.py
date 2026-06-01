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
