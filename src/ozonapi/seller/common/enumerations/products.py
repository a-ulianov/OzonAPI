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


class TurnoverGrade(str, Enum):
    """Фильтр по статусу ликвидности товаров.

    Attributes:
        TURNOVER_GRADE_NONE: нет статуса ликвидности
        DEFICIT: дефицитный. Остатков товара хватит до 28 дней
        POPULAR: очень популярный. Остатков товара хватит на 28–56 дней
        ACTUAL: популярный. Остатков товара хватит на 56–120 дней
        SURPLUS: избыточный. Товар продаётся медленно, остатков хватит более чем на 120 дней
        NO_SALES: без продаж. У товара нет продаж последние 28 дней
        WAS_NO_SALES: был без продаж. У товара не было продаж и остатков последние 28 дней
        RESTRICTED_NO_SALES: без продаж, ограничен. У товара не было продаж более 120 дней. Такой товар нельзя добавить в поставку
        COLLECTING_DATA: сбор данных. Для расчёта ликвидности нового товара собираем данные в течение 60 дней после поставки
        WAITING_FOR_SUPPLY: ожидаем поставки. На складе нет остатков, доступных к продаже. Сделайте поставку для начала сбора данных
        WAS_DEFICIT: был дефицитным. Товар был дефицитным последние 56 дней. Сейчас у него нет остатков
        WAS_POPULAR: был очень популярным. Товар был очень популярным последние 56 дней. Сейчас у него нет остатков
        WAS_ACTUAL: был популярным. Товар был популярным последние 56 дней. Сейчас у него нет остатков
        WAS_SURPLUS: был избыточным. Товар был избыточным последние 56 дней. Сейчас у него нет остатков
    """
    TURNOVER_GRADE_NONE = "TURNOVER_GRADE_NONE"
    DEFICIT = "DEFICIT"
    POPULAR = "POPULAR"
    ACTUAL = "ACTUAL"
    SURPLUS = "SURPLUS"
    NO_SALES = "NO_SALES"
    WAS_NO_SALES = "WAS_NO_SALES"
    RESTRICTED_NO_SALES = "RESTRICTED_NO_SALES"
    COLLECTING_DATA = "COLLECTING_DATA"
    WAITING_FOR_SUPPLY = "WAITING_FOR_SUPPLY"
    WAS_DEFICIT = "WAS_DEFICIT"
    WAS_POPULAR = "WAS_POPULAR"
    WAS_ACTUAL = "WAS_ACTUAL"
    WAS_SURPLUS = "WAS_SURPLUS"


class ItemTag(str, Enum):
    """Фильтр по тегам товара.

    Attributes:
        ITEM_ATTRIBUTE_NONE: без тега
        ECONOM: эконом-товар
        NOVEL: новинка
        DISCOUNT: уценённый товар
        FBS_RETURN: товар из возврата FBS
        SUPER: Super-товар
    """
    ITEM_ATTRIBUTE_NONE = "ITEM_ATTRIBUTE_NONE"
    ECONOM = "ECONOM"
    NOVEL = "NOVEL"
    DISCOUNT = "DISCOUNT"
    FBS_RETURN = "FBS_RETURN"
    SUPER = "SUPER"
