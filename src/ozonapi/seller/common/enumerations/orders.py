from enum import Enum


class OrderDeliverySchema(str, Enum):
    """Схема доставки при создании заказа.

    Attributes:
        MIX: На выбор Ozon
        FBO: Доставка со склада Ozon
        FBS: Доставка со склада продавца
    """
    MIX = "MIX"
    FBO = "FBO"
    FBS = "FBS"


class OrderDeliveryType(str, Enum):
    """Тип доставки при создании заказа.

    Attributes:
        COURIER: Доставка курьером
        PVZ: Доставка в пункт выдачи заказов
        POSTAMAT: Доставка в постамат
    """
    COURIER = "COURIER"
    PVZ = "PVZ"
    POSTAMAT = "POSTAMAT"
