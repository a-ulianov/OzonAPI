"""Описывает модели методов раздела Акции.
https://docs.ozon.ru/api/seller/#tag/Promos
"""
__all__ = [
    "ActionProduct",
    "ActionsProductsChangeRejected",
    "ActionsProductsChangeResult",
    "DiscountTaskFailDetail",
    "DiscountTaskResult",
    "DiscountTaskResponse",
    "ActionItem",
    "ActionsResponse",
    "ActionsCandidatesRequest",
    "ActionsCandidatesResult",
    "ActionsCandidatesResponse",
    "ActionsProductsRequest",
    "ActionsProductsResult",
    "ActionsProductsResponse",
    "ActionsProductsActivateProduct",
    "ActionsProductsActivateRequest",
    "ActionsProductsActivateResponse",
    "ActionsProductsDeactivateRequest",
    "ActionsProductsDeactivateResponse",
    "DiscountTask",
    "ActionsDiscountsTaskListRequest",
    "ActionsDiscountsTaskListResponse",
    "ActionsDiscountsTaskApproveTask",
    "ActionsDiscountsTaskApproveRequest",
    "ActionsDiscountsTaskDeclineTask",
    "ActionsDiscountsTaskDeclineRequest",
]

from .base import (
    ActionProduct,
    ActionsProductsChangeRejected,
    ActionsProductsChangeResult,
    DiscountTaskFailDetail,
    DiscountTaskResult,
    DiscountTaskResponse,
)
from .v1__actions import (
    ActionItem,
    ActionsResponse,
)
from .v1__actions_candidates import (
    ActionsCandidatesRequest,
    ActionsCandidatesResult,
    ActionsCandidatesResponse,
)
from .v1__actions_products import (
    ActionsProductsRequest,
    ActionsProductsResult,
    ActionsProductsResponse,
)
from .v1__actions_products_activate import (
    ActionsProductsActivateProduct,
    ActionsProductsActivateRequest,
    ActionsProductsActivateResponse,
)
from .v1__actions_products_deactivate import (
    ActionsProductsDeactivateRequest,
    ActionsProductsDeactivateResponse,
)
from .v1__actions_discounts_task_list import (
    DiscountTask,
    ActionsDiscountsTaskListRequest,
    ActionsDiscountsTaskListResponse,
)
from .v1__actions_discounts_task_approve import (
    ActionsDiscountsTaskApproveTask,
    ActionsDiscountsTaskApproveRequest,
)
from .v1__actions_discounts_task_decline import (
    ActionsDiscountsTaskDeclineTask,
    ActionsDiscountsTaskDeclineRequest,
)
