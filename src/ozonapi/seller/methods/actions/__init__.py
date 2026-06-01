__all__ = ["SellerActionsAPI", ]

from .actions import ActionsMixin
from .actions_auto_add_products_candidates import ActionsAutoAddProductsCandidatesMixin
from .actions_auto_add_products_delete import ActionsAutoAddProductsDeleteMixin
from .actions_auto_add_products_list import ActionsAutoAddProductsListMixin
from .actions_auto_add_products_update import ActionsAutoAddProductsUpdateMixin
from .actions_candidates import ActionsCandidatesMixin
from .actions_discounts_task_approve import ActionsDiscountsTaskApproveMixin
from .actions_discounts_task_decline import ActionsDiscountsTaskDeclineMixin
from .actions_discounts_task_list_v1 import ActionsDiscountsTaskListV1Mixin
from .actions_products import ActionsProductsMixin
from .actions_products_activate import ActionsProductsActivateMixin
from .actions_products_deactivate import ActionsProductsDeactivateMixin


class SellerActionsAPI(
    ActionsMixin,
    ActionsAutoAddProductsCandidatesMixin,
    ActionsAutoAddProductsDeleteMixin,
    ActionsAutoAddProductsListMixin,
    ActionsAutoAddProductsUpdateMixin,
    ActionsCandidatesMixin,
    ActionsDiscountsTaskApproveMixin,
    ActionsDiscountsTaskDeclineMixin,
    ActionsDiscountsTaskListV1Mixin,
    ActionsProductsMixin,
    ActionsProductsActivateMixin,
    ActionsProductsDeactivateMixin,
):
    """Реализует методы раздела Акции.

    References:
        https://docs.ozon.ru/api/seller/#tag/Promos
    """
    pass
