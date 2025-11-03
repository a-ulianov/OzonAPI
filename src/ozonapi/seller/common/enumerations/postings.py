from enum import Enum


class AvailablePostingActions(str, Enum):
    """Доступные действия и информация об отправлении.

    Attributes:
        ARBITRATION: открыть спор
        AWAITING_DELIVERY: перевести в статус «Ожидает отгрузки»
        CAN_CREATE_CHAT: открыть чат с покупателем
        CANCEL: отменить отправление
        CLICK_TRACK_NUMBER: просмотреть по трек-номеру историю изменения статусов в личном кабинете
        CUSTOMER_PHONE_AVAILABLE: телефон покупателя
        HAS_WEIGHT_PRODUCTS: весовые товары в отправлении
        HAS_BARCODE_FOR_PRINTING: штрихкод для печати
        HIDE_REGION_AND_CITY: скрыть регион и город покупателя в отчёте
        INVOICE_GET: получить информацию из счёта-фактуры
        INVOICE_SEND: создать счёт-фактуру
        INVOICE_UPDATE: отредактировать счёт-фактуру
        LABEL_DOWNLOAD_BIG: скачать большую этикетку
        LABEL_DOWNLOAD_SMALL: скачать маленькую этикетку
        LABEL_DOWNLOAD: скачать этикетку
        NON_INT_DELIVERED: перевести в статус Условно доставлен
        NON_INT_DELIVERING: перевести в статус Доставляется
        NON_INT_LAST_MILE: перевести в статус Курьер в пути
        PRODUCT_CANCEL: отменить часть товаров в отправлении
        SET_CUTOFF: необходимо указать дату отгрузки, воспользуйтесь методом posting_cutoff_set()
        SET_TIMESLOT: изменить время доставки покупателю
        SET_TRACK_NUMBER: указать или изменить трек-номер
        SHIP_ASYNC_IN_PROCESS: отправление собирается
        SHIP_ASYNC_RETRY: собрать отправление повторно после ошибки сборки
        SHIP_ASYNC: собрать отправление
        SHIP_WITH_ADDITIONAL_INFO: необходимо заполнить дополнительную информацию
        SHIP: собрать отправление
        UPDATE_CIS: изменить дополнительную информацию
    """
    ARBITRATION = "arbitration"
    AWAITING_DELIVERY = "awaiting_delivery"
    CAN_CREATE_CHAT = "can_create_chat"
    CANCEL = "cancel"
    CLICK_TRACK_NUMBER = "click_track_number"
    CUSTOMER_PHONE_AVAILABLE = "customer_phone_available"
    HAS_WEIGHT_PRODUCTS = "has_weight_products"
    HAS_BARCODE_FOR_PRINTING = "has_barcode_for_printing"
    HIDE_REGION_AND_CITY = "hide_region_and_city"
    INVOICE_GET = "invoice_get"
    INVOICE_SEND = "invoice_send"
    INVOICE_UPDATE = "invoice_update"
    LABEL_DOWNLOAD_BIG = "label_download_big"
    LABEL_DOWNLOAD_SMALL = "label_download_small"
    LABEL_DOWNLOAD = "label_download"
    NON_INT_DELIVERED = "non_int_delivered"
    NON_INT_DELIVERING = "non_int_delivering"
    NON_INT_LAST_MILE = "non_int_last_mile"
    PRODUCT_CANCEL = "product_cancel"
    SET_CUTOFF = "set_cutoff"
    SET_TIMESLOT = "set_timeslot"
    SET_TRACK_NUMBER = "set_track_number"
    SHIP_ASYNC_IN_PROCESS = "ship_async_in_process"
    SHIP_ASYNC_RETRY = "ship_async_retry"
    SHIP_ASYNC = "ship_async"
    SHIP_WITH_ADDITIONAL_INFO = "ship_with_additional_info"
    SHIP = "ship"
    UPDATE_CIS = "update_cis"


class PostingStatus(str, Enum):
    """Статус отправления.

    Attributes:
        ACCEPTANCE_IN_PROGRESS: идёт приёмка
        AWAITING_APPROVE: ожидает подтверждения
        AWAITING_PACKAGING: ожидает упаковки
        AWAITING_REGISTRATION: ожидает регистрации
        AWAITING_DELIVER: ожидает отгрузки
        ARBITRATION: арбитраж
        CLIENT_ARBITRATION: клиентский арбитраж доставки
        DELIVERED: доставлено
        DELIVERING: доставляется
        DRIVER_PICKUP: у водителя
        NOT_ACCEPTED: не принят на сортировочном центре
        AWAITING_VERIFICATION: создано
        CANCELLED: отменено
        CANCELLED_FROM_SPLIT_PENDING: отменён из-за разделения отправления
        SENT_BY_SELLER: отправлено продавцом
    """
    ACCEPTANCE_IN_PROGRESS = "acceptance_in_progress"
    AWAITING_APPROVE = "awaiting_approve"
    AWAITING_PACKAGING = "awaiting_packaging"
    AWAITING_REGISTRATION = "awaiting_registration"
    AWAITING_DELIVER = "awaiting_deliver"
    ARBITRATION = "arbitration"
    CLIENT_ARBITRATION = "client_arbitration"
    DELIVERED = "delivered"
    DELIVERING = "delivering"
    DRIVER_PICKUP = "driver_pickup"
    NOT_ACCEPTED = "not_accepted"
    AWAITING_VERIFICATION = "awaiting_verification"
    CANCELLED = "cancelled"
    CANCELLED_FROM_SPLIT_PENDING = "cancelled_from_split_pending"
    SENT_BY_SELLER = "sent_by_seller"


class PostingSubstatus(str, Enum):
    """Подстатус отправления.

    Attributes:
        POSTING_ACCEPTANCE_IN_PROGRESS: идёт приёмка
        POSTING_IN_ARBITRATION: арбитраж
        POSTING_CREATED: создано
        POSTING_IN_CARRIAGE: в перевозке
        POSTING_NOT_IN_CARRIAGE: не добавлено в перевозку
        POSTING_REGISTERED: зарегистрировано
        POSTING_TRANSFERRING_TO_DELIVERY: передаётся в доставку
        POSTING_AWAITING_PASSPORT_DATA: ожидает паспортных данных
        POSTING_AWAITING_REGISTRATION: ожидает регистрации
        POSTING_REGISTRATION_ERROR: ошибка регистрации
        POSTING_SPLIT_PENDING: создано
        POSTING_CANCELED: отменено
        POSTING_IN_CLIENT_ARBITRATION: клиентский арбитраж доставки
        POSTING_DELIVERED: доставлено
        POSTING_RECEIVED: получено
        POSTING_CONDITIONALLY_DELIVERED: условно доставлено
        POSTING_IN_COURIER_SERVICE: курьер в пути
        POSTING_IN_PICKUP_POINT: в пункте выдачи
        POSTING_ON_WAY_TO_CITY: в пути в ваш город
        POSTING_ON_WAY_TO_PICKUP_POINT: в пути в пункт выдачи
        POSTING_RETURNED_TO_WAREHOUSE: возвращено на склад
        POSTING_TRANSFERRED_TO_COURIER_SERVICE: передаётся в службу доставки
        POSTING_DRIVER_PICK_UP: у водителя
        POSTING_NOT_IN_SORT_CENTER: не принято на сортировочном центре
        SHIP_FAILED: неудачная отправка
    """
    POSTING_ACCEPTANCE_IN_PROGRESS = "posting_acceptance_in_progress"
    POSTING_IN_ARBITRATION = "posting_in_arbitration"
    POSTING_CREATED = "posting_created"
    POSTING_IN_CARRIAGE = "posting_in_carriage"
    POSTING_NOT_IN_CARRIAGE = "posting_not_in_carriage"
    POSTING_REGISTERED = "posting_registered"
    POSTING_TRANSFERRING_TO_DELIVERY = "posting_transferring_to_delivery"
    POSTING_AWAITING_PASSPORT_DATA = "posting_awaiting_passport_data"
    POSTING_AWAITING_REGISTRATION = "posting_awaiting_registration"
    POSTING_REGISTRATION_ERROR = "posting_registration_error"
    POSTING_SPLIT_PENDING = "posting_split_pending"
    POSTING_CANCELED = "posting_canceled"
    POSTING_IN_CLIENT_ARBITRATION = "posting_in_client_arbitration"
    POSTING_DELIVERED = "posting_delivered"
    POSTING_RECEIVED = "posting_received"
    POSTING_CONDITIONALLY_DELIVERED = "posting_conditionally_delivered"
    POSTING_IN_COURIER_SERVICE = "posting_in_courier_service"
    POSTING_IN_PICKUP_POINT = "posting_in_pickup_point"
    POSTING_ON_WAY_TO_CITY = "posting_on_way_to_city"
    POSTING_ON_WAY_TO_PICKUP_POINT = "posting_on_way_to_pickup_point"
    POSTING_RETURNED_TO_WAREHOUSE = "posting_returned_to_warehouse"
    POSTING_TRANSFERRED_TO_COURIER_SERVICE = "posting_transferred_to_courier_service"
    POSTING_DRIVER_PICK_UP = "posting_driver_pick_up"
    POSTING_NOT_IN_SORT_CENTER = "posting_not_in_sort_center"
    SHIP_FAILED = "ship_failed"


class CancellationType(str, Enum):
    """Тип отмены отправления.

    Attributes:
        SELLER: отменено продавцом
        CLIENT: отменено покупателем
        CUSTOMER: отменено покупателем
        OZON: отменено Ozon
        SYSTEM: отменено системой
        DELIVERY: отменено службой доставки
        UNSPECIFIED: не указано
    """
    SELLER = "seller"
    CLIENT = "client"
    CUSTOMER = "customer"
    OZON = "ozon"
    SYSTEM = "system"
    DELIVERY = "delivery"
    UNSPECIFIED = ""


class CancellationReasonTypeId(str, Enum):
    """Инициатор отмены отправления.

    Attributes:
        BUYER: покупатель
        SELLER: продавец
    """
    BUYER = "buyer"
    SELLER = "seller"


class LabelFormingStatus(str, Enum):
    """Статус формирования этикеток.

    Attributes:
        PENDING: задание в очереди
        IN_PROGRESS: формируются
        COMPLETED: файл с этикетками готов
        ERROR: ошибка при создании файла
        UNSPECIFIED: не определено
    """
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ERROR = "error"
    UNSPECIFIED = ""


class LabelType(str, Enum):
    """Типы этикеток.

    Attributes:
        BIG_LABEL: Обычная этикетка
        SMALL_LABEL: Маленькая этикетка
    """
    BIG_LABEL = "big_label"
    SMALL_LABEL = "small_label"


class MarkType(str, Enum):
    """Тип кода маркировки.

    Attributes:
        MANDATORY_MARK: обязательная маркировка «Честный ЗНАК»
        JW_UIN: уникальный идентификационный номер (УИН) ювелирного изделия
        IMEI: IMEI мобильного устройства
    """
    MANDATORY_MARK = "mandatory_mark"
    JW_UIN = "jw_uin"
    IMEI = "imei"


class PaymentTypeGroupName(str, Enum):
    """Тип оплаты.
    OZON_CARD: Ozon Карта
    OZON_CARD_AUTO_DEBIT_AT_ISSUANCE: автосписание с Ozon Карты при выдаче
    SAVED_CARD_AT_ISSUANCE: сохранённой картой при получении
    SBP: Система Быстрых Платежей
    OZON_INSTALLMENT: Ozon Рассрочка
    BANK_ACCOUNT: оплата на расчётный счёт
    SBERPAY: SberPay
    UNSPECIFIED: не указано
    """
    CARD_ONLINE = "картой онлайн"
    OZON_CARD = "Ozon Карта"
    OZON_CARD_AUTO_DEBIT_AT_ISSUANCE = "автосписание с Ozon Карты при выдаче"
    SAVED_CARD_AT_ISSUANCE = "сохранённой картой при получении"
    SBP = "Система Быстрых Платежей"
    OZON_INSTALLMENT = "Ozon Рассрочка"
    BANK_ACCOUNT = "оплата на расчётный счёт"
    SBERPAY = "SberPay"
    UNSPECIFIED = ""


class PrrOption(str, Enum):
    """Код услуги погрузочно-разгрузочных работ

    Attributes:
        LIFT: подъём на лифте
        STAIRS: подъём по лестнице
        FLOOR: подъем на этаж
        NONE: покупатель отказался от услуги, поднимать товары не нужно
        DELIVERY_DEFAULT: доставка включена в стоимость, по условиям оферты нужно доставить товар на этаж
        UNSPECIFIED: не указано
    """
    LIFT = "lift"
    STAIRS = "stairs"
    NONE = "none"
    DELIVERY_DEFAULT = "delivery_default"
    UNSPECIFIED = ""


class PostingShipmentStatus(str, Enum):
    """Статус проверки всех экземпляров отправления и доступности сборки.

    Attributes:
        SHIP_AVAILABLE: сборка доступна
        SHIP_NOT_AVAILABLE: сборка недоступна
        VALIDATION_IN_PROCESS: экземпляры на проверке
        UPDATE_AVAILABLE: разрешено редактировать данные по экземплярам
        UPDATE_NOT_AVAILABLE: запрещено редактировать данные по экземплярам
    """
    SHIP_AVAILABLE = "ship_available"
    SHIP_NOT_AVAILABLE = "ship_not_available"
    VALIDATION_IN_PROCESS = "validation_in_process"
    UPDATE_AVAILABLE = "update_available"
    UPDATE_NOT_AVAILABLE = "update_not_available"


class TplIntegrationType(str, Enum):
    """Тип интеграции со службой доставки

    Attributes:
        OZON: доставка службой Ozon
        _3PL_TRACKING: доставка интегрированной службой
        NON_INTEGRATED: доставка сторонней службой
        AGGREGATOR: доставка через партнёрскую доставку Ozon
        HYBRYD: схема доставки Почты России
    """
    OZON = "ozon"
    _3PL_TRACKING = "3pl_tracking"
    NON_INTEGRATED = "non_integrated"
    AGGREGATOR = "aggregator"
    HYBRYD = "hybryd"