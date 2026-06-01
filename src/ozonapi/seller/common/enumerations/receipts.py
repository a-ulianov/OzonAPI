from enum import Enum


class ReceiptType(str, Enum):
    """Тип чека.

    Attributes:
        UNSPECIFIED: не определён
        INCOMING: чек реализации
        REFUND: чек возврата
    """
    UNSPECIFIED = "UNSPECIFIED"
    INCOMING = "INCOMING"
    REFUND = "REFUND"


class ReceiptOperationType(str, Enum):
    """Тип операции.

    Attributes:
        UNSPECIFIED: не определён
        COMMODITY: товарная операция
    """
    UNSPECIFIED = "UNSPECIFIED"
    COMMODITY = "COMMODITY"
