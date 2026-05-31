"""Композиция миксинов методов раздела Отчёты.

Объединяет методы работы с отчётами продавца в единый класс :class:`SellerReportAPI`.
"""

from ...core import APIManager
from .finance_cash_flow_statement_list import FinanceCashFlowStatementListMixin
from .report_discounted_create import ReportDiscountedCreateMixin
from .report_info import ReportInfoMixin
from .report_list import ReportListMixin
from .report_marked_products_sales_create import ReportMarkedProductsSalesCreateMixin
from .report_placement_by_products_create import ReportPlacementByProductsCreateMixin
from .report_placement_by_supplies_create import ReportPlacementBySuppliesCreateMixin
from .report_postings_create import ReportPostingsCreateMixin
from .report_products_create import ReportProductsCreateMixin
from .report_returns_create import ReportReturnsCreateMixin
from .report_warehouse_stock import ReportWarehouseStockMixin


class SellerReportAPI(
    FinanceCashFlowStatementListMixin,
    ReportDiscountedCreateMixin,
    ReportInfoMixin,
    ReportListMixin,
    ReportMarkedProductsSalesCreateMixin,
    ReportPlacementByProductsCreateMixin,
    ReportPlacementBySuppliesCreateMixin,
    ReportPostingsCreateMixin,
    ReportProductsCreateMixin,
    ReportReturnsCreateMixin,
    ReportWarehouseStockMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Отчёты.

    Notes:
        • Объединяет методы создания отчётов (товары, отправления, возвраты, остатки,
          размещение, маркировка), получения информации и списка отчётов, а также
          финансового отчёта о движении денежных средств.

    References:
        • https://docs.ozon.ru/api/seller/#tag/ReportAPI
    """

    pass
