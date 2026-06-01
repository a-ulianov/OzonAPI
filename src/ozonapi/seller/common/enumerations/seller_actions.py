from enum import Enum


class SellerActionDiscountType(str, Enum):
    """Тип скидки в акции продавца (для запросов создания акции).

    Attributes:
        PERCENT: скидка в процентах
        CURRENCY: скидка в валюте
    """
    PERCENT = "PERCENT"
    CURRENCY = "CURRENCY"


class SellerActionVoucherType(str, Enum):
    """Тип промокода для акции с механикой «Скидка по промокоду».

    Attributes:
        ONE: один промокод на всех покупателей
        MULTIPLE: несколько одинаковых промокодов
        UNIQUE: уникальные промокоды для каждого покупателя
    """
    ONE = "ONE"
    MULTIPLE = "MULTIPLE"
    UNIQUE = "UNIQUE"


class SellerActionType(str, Enum):
    """Механика акции продавца (фильтр в запросе списка акций).

    Attributes:
        DISCOUNT: скидка
        VOUCHER_DISCOUNT: скидка по промокоду
        DISCOUNT_WITH_CONDITION: скидка от суммы заказа
        INSTALLMENT: беспроцентная рассрочка
        INDIVIDUAL_DISCOUNT_BY_PRODUCTS: индивидуальная скидка на товары
        OZON_ACCOUNT_DISCOUNT: скидка по Ozon Счёту
        MULTI_LEVEL_DISCOUNT_ON_AMOUNT: многоуровневая скидка от суммы
    """
    DISCOUNT = "DISCOUNT"
    VOUCHER_DISCOUNT = "VOUCHER_DISCOUNT"
    DISCOUNT_WITH_CONDITION = "DISCOUNT_WITH_CONDITION"
    INSTALLMENT = "INSTALLMENT"
    INDIVIDUAL_DISCOUNT_BY_PRODUCTS = "INDIVIDUAL_DISCOUNT_BY_PRODUCTS"
    OZON_ACCOUNT_DISCOUNT = "OZON_ACCOUNT_DISCOUNT"
    MULTI_LEVEL_DISCOUNT_ON_AMOUNT = "MULTI_LEVEL_DISCOUNT_ON_AMOUNT"


class SellerActionStatus(str, Enum):
    """Статус акции продавца (фильтр в запросе списка акций).

    Attributes:
        ACTIVE: активна
        ENDED: завершена
        PLANNED: запланирована
        PAUSED: приостановлена
    """
    ACTIVE = "ACTIVE"
    ENDED = "ENDED"
    PLANNED = "PLANNED"
    PAUSED = "PAUSED"
