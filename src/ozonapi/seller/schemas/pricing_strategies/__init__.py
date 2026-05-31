"""Описывает модели методов раздела Стратегии ценообразования.
https://docs.ozon.ru/api/seller/#tag/PricingStrategyAPI
"""
__all__ = [
    "StrategyCompetitor",
    "StrategyProductError",
    "StrategyCompetitorsListRequest",
    "StrategyCompetitorItem",
    "StrategyCompetitorsListResponse",
    "StrategyCreateRequest",
    "StrategyCreateResult",
    "StrategyCreateResponse",
    "StrategyDeleteRequest",
    "StrategyDeleteResponse",
    "StrategyInfoRequest",
    "StrategyInfoResult",
    "StrategyInfoResponse",
    "StrategyListRequest",
    "StrategyListItem",
    "StrategyListResponse",
    "StrategyProductInfoRequest",
    "StrategyProductInfoResult",
    "StrategyProductInfoResponse",
    "StrategyProductsAddRequest",
    "StrategyProductsAddResult",
    "StrategyProductsAddResponse",
    "StrategyProductsDeleteRequest",
    "StrategyProductsDeleteResult",
    "StrategyProductsDeleteResponse",
    "StrategyProductsListRequest",
    "StrategyProductsListResult",
    "StrategyProductsListResponse",
    "StrategyStatusRequest",
    "StrategyStatusResponse",
    "StrategyIdsByProductIdsRequest",
    "StrategyProductStrategyItem",
    "StrategyIdsByProductIdsResult",
    "StrategyIdsByProductIdsResponse",
    "StrategyUpdateRequest",
    "StrategyUpdateResponse",
]

from .base import StrategyCompetitor, StrategyProductError
from .v1__strategy_competitors_list import (
    StrategyCompetitorsListRequest,
    StrategyCompetitorItem,
    StrategyCompetitorsListResponse,
)
from .v1__strategy_create import (
    StrategyCreateRequest,
    StrategyCreateResult,
    StrategyCreateResponse,
)
from .v1__strategy_delete import (
    StrategyDeleteRequest,
    StrategyDeleteResponse,
)
from .v1__strategy_info import (
    StrategyInfoRequest,
    StrategyInfoResult,
    StrategyInfoResponse,
)
from .v1__strategy_list import (
    StrategyListRequest,
    StrategyListItem,
    StrategyListResponse,
)
from .v1__strategy_product_info import (
    StrategyProductInfoRequest,
    StrategyProductInfoResult,
    StrategyProductInfoResponse,
)
from .v1__strategy_products_add import (
    StrategyProductsAddRequest,
    StrategyProductsAddResult,
    StrategyProductsAddResponse,
)
from .v1__strategy_products_delete import (
    StrategyProductsDeleteRequest,
    StrategyProductsDeleteResult,
    StrategyProductsDeleteResponse,
)
from .v1__strategy_products_list import (
    StrategyProductsListRequest,
    StrategyProductsListResult,
    StrategyProductsListResponse,
)
from .v1__strategy_status import (
    StrategyStatusRequest,
    StrategyStatusResponse,
)
from .v1__strategy_ids_by_product_ids import (
    StrategyIdsByProductIdsRequest,
    StrategyProductStrategyItem,
    StrategyIdsByProductIdsResult,
    StrategyIdsByProductIdsResponse,
)
from .v1__strategy_update import (
    StrategyUpdateRequest,
    StrategyUpdateResponse,
)
