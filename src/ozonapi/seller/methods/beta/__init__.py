__all__ = ["SellerBetaAPI", ]

from .actions_discounts_task_list import ActionsDiscountsTaskListMixin
from .analytics_manage_stocks import AnalyticsManageStocksMixin
from .analytics_stocks import AnalyticsStocksMixin
from .cluster_list import ClusterListMixin
from .finance_accrual_by_day import FinanceAccrualByDayMixin
from .finance_accrual_postings import FinanceAccrualPostingsMixin
from .finance_accrual_types import FinanceAccrualTypesMixin
from .finance_balance import FinanceBalanceMixin
from .posting_digital_list import PostingDigitalListMixin
from .product_stairway_discount_by_quantity_get import (
    ProductStairwayDiscountByQuantityGetMixin,
)
from .product_stairway_discount_by_quantity_set import (
    ProductStairwayDiscountByQuantitySetMixin,
)
from .product_visibility_info import ProductVisibilityInfoMixin
from .product_visibility_set import ProductVisibilitySetMixin
from .removal_from_stock_list import RemovalFromStockListMixin
from .removal_from_supply_list import RemovalFromSupplyListMixin
from .seller_info import SellerInfoMixin


class SellerBetaAPI(
    ActionsDiscountsTaskListMixin,
    AnalyticsManageStocksMixin,
    AnalyticsStocksMixin,
    ClusterListMixin,
    FinanceAccrualByDayMixin,
    FinanceAccrualPostingsMixin,
    FinanceAccrualTypesMixin,
    FinanceBalanceMixin,
    PostingDigitalListMixin,
    ProductStairwayDiscountByQuantityGetMixin,
    ProductStairwayDiscountByQuantitySetMixin,
    ProductVisibilityInfoMixin,
    ProductVisibilitySetMixin,
    RemovalFromStockListMixin,
    RemovalFromSupplyListMixin,
    SellerInfoMixin,
):
    """Реализует методы раздела Прочие методы.

    References:
        https://docs.ozon.com/api/seller/?#tag/BetaMethod
    """
    pass
