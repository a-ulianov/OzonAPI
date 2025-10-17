from enum import Enum


class Availability(str, Enum):
    """Признак доступности товара по SKU.

    Attributes:
        HIDDEN: скрыт
        AVAILABLE: доступен
        UNAVAILABLE: недоступен, SKU удалён
    """
    HIDDEN = "HIDDEN"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class ColorIndex(str, Enum):
    """Итоговый индекс цены товара.

    Attributes:
        UNSPECIFIED: не определен
        WITHOUT_INDEX: нет индекса
        GREEN: выгодный
        YELLOW: умеренный
        RED: невыгодный
        SUPER: супер-индекс (не указано значение в документации)
    """
    UNSPECIFIED = "COLOR_INDEX_UNSPECIFIED"
    WITHOUT_INDEX = "WITHOUT_INDEX"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    SUPER = "SUPER"


class DeliverySchema(str, Enum):
    """Схема доставки

    Attributes:
        SDS: идентификатор единого Ozon SKU
        FBO: идентификатор товара, который продаётся со склада Ozon
        FBS: идентификатор товара, который продаётся со склада FBS
        CROSSBORDER: идентификатор товара, который продаётся из-за границы
    """
    SDS = "SDS"
    FBO = "FBO"
    FBS = "FBS"
    CROSSBORDER = "Crossborder"


class DimensionUnit(str, Enum):
    """Единицы измерения габаритов.

    Attributes:
        MILLIMETERS: миллиметры
        CENTIMETERS: сантиметры
        INCHES: дюймы
    """
    MILLIMETERS = "mm"
    CENTIMETERS = "cm"
    INCHES = "in"


class ErrorLevel(str, Enum):
    """Уровень ошибки.

    Attributes:
        UNSPECIFIED: не определён
        ERROR: критичная ошибка, товар нельзя продавать
        WARNING: некритичная ошибка, товар можно продавать
        INTERNAL: критичная ошибка, товар нельзя продавать
    """
    UNSPECIFIED = "ERROR_LEVEL_UNSPECIFIED"
    ERROR = "ERROR_LEVEL_ERROR"
    WARNING = "ERROR_LEVEL_WARNING"
    INTERNAL = "ERROR_LEVEL_INTERNAL"

class ProductHandlingStatus(str, Enum):
    """Статус создания или обновления товара.

    Attributes:
        PENDING: товар в очереди на обработку
        IMPORTED: товар успешно загружен
        FAILED: товар загружен с ошибками
        SKIPPED: товар не был обновлен, так как запрос не содержал изменений
    """
    PENDING = "pending"
    IMPORTED = "imported"
    FAILED = "failed"
    SKIPPED = "skipped"


class PromotionOperation(str, Enum):
    """Действия с акцией.

    Attributes:
        ENABLE: включить
        DISABLE: выключить
        UNKNOWN: ничего не менять
    """
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    UNKNOWN = "UNKNOWN"


class PromotionType(str, Enum):
    """Типы акций.

    Attributes:
        REVIEWS_PROMO: баллы за отзывы
    """
    REVIEWS_PROMO = "REVIEWS_PROMO"


class ServiceType(str, Enum):
    """Типы сервиса (описание отсутствует в документации).

    Attributes:
        IS_CODE_SERVICE: сервис с кодом
        IS_NO_CODE_SERVICE: сервис без кода
    """
    IS_CODE_SERVICE = "IS_CODE_SERVICE"
    IS_NO_CODE_SERVICE = "IS_NO_CODE_SERVICE"


class ShipmentType(str, Enum):
    """Типы упаковки.

    Attributes:
        UNSPECIFIED: не указано
        GENERAL: обычный товар
        BOX: коробка
        PALLET: палета
    """
    UNSPECIFIED = "SHIPMENT_TYPE_UNSPECIFIED"
    GENERAL = "SHIPMENT_TYPE_GENERAL"
    BOX = "SHIPMENT_TYPE_BOX"
    PALLET = "SHIPMENT_TYPE_PALLET"


class VAT(str, Enum):
    """Ставка НДС для товара.

    Attributes:
        PERCENT_0: НДС не облагается
        PERCENT_5: НДС 5%
        PERCENT_7: НДС 7%
        PERCENT_10: НДС 10%
        PERCENT_20: НДС 20%
        PERCENT_22: НДС 22%
    """
    PERCENT_0 = "0"
    PERCENT_5 = "0.05"
    PERCENT_7 = "0.07"
    PERCENT_10 = "0.10"
    PERCENT_20 = "0.20"
    PERCENT_22 = "0.22"


class Visibility(str, Enum):
    """Фильтр по видимости товара.

    Attributes:
        ALL: все товары
        VISIBLE: товары, которые видны покупателям
        INVISIBLE: товары, которые не видны покупателям
        EMPTY_STOCK: товары, у которых не указано наличие
        NOT_MODERATED: товары, которые не прошли модерацию
        MODERATED: товары, которые прошли модерацию
        DISABLED: товары, которые видны покупателям, но недоступны к покупке
        STATE_FAILED: товары, создание которых завершилось ошибкой
        READY_TO_SUPPLY: товары, готовые к поставке
        VALIDATION_STATE_PENDING: товары, которые проходят проверку валидатором на премодерации
        VALIDATION_STATE_FAIL: товары, которые не прошли проверку валидатором на премодерации
        VALIDATION_STATE_SUCCESS: товары, которые прошли проверку валидатором на премодерации
        TO_SUPPLY: товары, готовые к продаже
        IN_SALE: товары в продаже
        REMOVED_FROM_SALE: товары, скрытые от покупателей
        BANNED: заблокированные товары
        OVERPRICED: товары с завышенной ценой
        CRITICALLY_OVERPRICED: товары со слишком завышенной ценой
        EMPTY_BARCODE: товары без штрихкода
        BARCODE_EXISTS: товары со штрихкодом
        QUARANTINE: товары на карантине после изменения цены более чем на 50 %
        ARCHIVED: товары в архиве
        OVERPRICED_WITH_STOCK: товары в продаже со стоимостью выше, чем у конкурентов
        PARTIAL_APPROVED: товары в продаже с пустым или неполным описанием
    """
    ALL = "ALL"
    VISIBLE = "VISIBLE"
    INVISIBLE = "INVISIBLE"
    EMPTY_STOCK = "EMPTY_STOCK"
    NOT_MODERATED = "NOT_MODERATED"
    MODERATED = "MODERATED"
    DISABLED = "DISABLED"
    STATE_FAILED = "STATE_FAILED"
    READY_TO_SUPPLY = "READY_TO_SUPPLY"
    VALIDATION_STATE_PENDING = "VALIDATION_STATE_PENDING"
    VALIDATION_STATE_FAIL = "VALIDATION_STATE_FAIL"
    VALIDATION_STATE_SUCCESS = "VALIDATION_STATE_SUCCESS"
    TO_SUPPLY = "TO_SUPPLY"
    IN_SALE = "IN_SALE"
    REMOVED_FROM_SALE = "REMOVED_FROM_SALE"
    BANNED = "BANNED"
    OVERPRICED = "OVERPRICED"
    CRITICALLY_OVERPRICED = "CRITICALLY_OVERPRICED"
    EMPTY_BARCODE = "EMPTY_BARCODE"
    BARCODE_EXISTS = "BARCODE_EXISTS"
    QUARANTINE = "QUARANTINE"
    ARCHIVED = "ARCHIVED"
    OVERPRICED_WITH_STOCK = "OVERPRICED_WITH_STOCK"
    PARTIAL_APPROVED = "PARTIAL_APPROVED"


class WeightUnit(str, Enum):
    """Единицы измерения веса.

    Attributes:
        GRAMS: граммы
        KILOGRAMS: килограммы
        POUNDS: фунты
    """
    GRAMS = "g"
    KILOGRAMS = "kg"
    POUNDS = "lb"