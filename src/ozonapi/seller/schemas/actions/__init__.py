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
    "ActionsDiscountsTaskListV1Request",
    "ActionsDiscountsTaskListV1Response",
    "ActionsDiscountsTaskApproveTask",
    "ActionsDiscountsTaskApproveRequest",
    "ActionsDiscountsTaskDeclineTask",
    "ActionsDiscountsTaskDeclineRequest",
    "ActionsAutoAddProduct",
    "ActionsAutoAddPriceEntry",
    "ActionsAutoAddRejected",
    "ActionsAutoAddProductsCandidatesRequest",
    "ActionsAutoAddProductsCandidatesResponse",
    "ActionsAutoAddProductsListRequest",
    "ActionsAutoAddProductsListResponse",
    "ActionsAutoAddProductsDeleteRequest",
    "ActionsAutoAddProductsDeleteResponse",
    "ActionsAutoAddProductsUpdateProduct",
    "ActionsAutoAddProductsUpdateRequest",
    "ActionsAutoAddProductsUpdateResponse",
]

from .base import (
    ActionProduct,
    ActionsAutoAddPriceEntry,
    ActionsAutoAddProduct,
    ActionsAutoAddRejected,
    ActionsProductsChangeRejected,
    ActionsProductsChangeResult,
    DiscountTaskFailDetail,
    DiscountTaskResult,
    DiscountTaskResponse,
)
from .v1__actions_auto_add_products_candidates import (
    ActionsAutoAddProductsCandidatesRequest,
    ActionsAutoAddProductsCandidatesResponse,
)
from .v1__actions_auto_add_products_list import (
    ActionsAutoAddProductsListRequest,
    ActionsAutoAddProductsListResponse,
)
from .v1__actions_auto_add_products_delete import (
    ActionsAutoAddProductsDeleteRequest,
    ActionsAutoAddProductsDeleteResponse,
)
from .v1__actions_auto_add_products_update import (
    ActionsAutoAddProductsUpdateProduct,
    ActionsAutoAddProductsUpdateRequest,
    ActionsAutoAddProductsUpdateResponse,
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
    ActionsDiscountsTaskListV1Request,
    ActionsDiscountsTaskListV1Response,
)
from .v1__actions_discounts_task_approve import (
    ActionsDiscountsTaskApproveTask,
    ActionsDiscountsTaskApproveRequest,
)
from .v1__actions_discounts_task_decline import (
    ActionsDiscountsTaskDeclineTask,
    ActionsDiscountsTaskDeclineRequest,
)
