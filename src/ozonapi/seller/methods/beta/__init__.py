__all__ = ["SellerBetaAPI", ]

from .analytics_stocks import AnalyticsStocksMixin
from .seller_info import SellerInfoMixin


class SellerBetaAPI(
    AnalyticsStocksMixin,
    SellerInfoMixin,
):
    """Реализует методы раздела Прочие методы.

    References:
        https://docs.ozon.com/api/seller/?#tag/BetaMethod
    """
    pass