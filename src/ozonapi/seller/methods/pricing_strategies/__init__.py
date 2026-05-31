__all__ = ["SellerPricingStrategyAPI"]

from .strategy_competitors_list import StrategyCompetitorsListMixin
from .strategy_create import StrategyCreateMixin
from .strategy_delete import StrategyDeleteMixin
from .strategy_ids_by_product_ids import StrategyIdsByProductIdsMixin
from .strategy_info import StrategyInfoMixin
from .strategy_list import StrategyListMixin
from .strategy_product_info import StrategyProductInfoMixin
from .strategy_products_add import StrategyProductsAddMixin
from .strategy_products_delete import StrategyProductsDeleteMixin
from .strategy_products_list import StrategyProductsListMixin
from .strategy_status import StrategyStatusMixin
from .strategy_update import StrategyUpdateMixin


class SellerPricingStrategyAPI(
    StrategyCompetitorsListMixin,
    StrategyCreateMixin,
    StrategyDeleteMixin,
    StrategyIdsByProductIdsMixin,
    StrategyInfoMixin,
    StrategyListMixin,
    StrategyProductInfoMixin,
    StrategyProductsAddMixin,
    StrategyProductsDeleteMixin,
    StrategyProductsListMixin,
    StrategyStatusMixin,
    StrategyUpdateMixin,
):
    """Реализует методы раздела Стратегии ценообразования.

    References:
        https://docs.ozon.ru/api/seller/#tag/PricingStrategyAPI
    """

    pass
