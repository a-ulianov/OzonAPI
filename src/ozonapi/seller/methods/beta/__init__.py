__all__ = ["SellerBetaAPI", ]

from .analytics_stocks import AnalyticsStocksMixin


class SellerBetaAPI(
    AnalyticsStocksMixin,
):
    """Реализует методы раздела Прочие методы.

    References:
        https://docs.ozon.com/api/seller/?#tag/BetaMethod
    """
    pass