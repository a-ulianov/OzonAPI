"""Композиция миксинов методов раздела Финансовые отчёты.

Объединяет финансовые методы продавца в единый класс :class:`SellerFinanceAPI`.
"""

from ...core import APIManager
from .finance_compensation import FinanceCompensationMixin
from .finance_decompensation import FinanceDecompensationMixin
from .finance_document_b2b_sales import FinanceDocumentB2BSalesMixin
from .finance_document_b2b_sales_json import FinanceDocumentB2BSalesJSONMixin
from .finance_mutual_settlement import FinanceMutualSettlementMixin
from .finance_products_buyout import FinanceProductsBuyoutMixin
from .finance_realization import FinanceRealizationMixin
from .finance_realization_by_day import FinanceRealizationByDayMixin
from .finance_realization_posting import FinanceRealizationPostingMixin
from .finance_transaction_list import FinanceTransactionListMixin
from .finance_transaction_totals import FinanceTransactionTotalsMixin


class SellerFinanceAPI(
    FinanceCompensationMixin,
    FinanceDecompensationMixin,
    FinanceDocumentB2BSalesMixin,
    FinanceDocumentB2BSalesJSONMixin,
    FinanceMutualSettlementMixin,
    FinanceProductsBuyoutMixin,
    FinanceRealizationMixin,
    FinanceRealizationByDayMixin,
    FinanceRealizationPostingMixin,
    FinanceTransactionListMixin,
    FinanceTransactionTotalsMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Финансовые отчёты.

    Notes:
        • Объединяет методы отчётов о реализации (по месяцам и отправлениям),
          списка и итогов транзакций, продаж юридическим лицам, взаиморасчётов,
          выкупов, компенсаций и декомпенсаций.

    References:
        • https://docs.ozon.ru/api/seller/#tag/FinanceAPI
    """

    pass
