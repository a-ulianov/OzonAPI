__all__ = ["SellerActionsAPI", ]

from .actions import ActionsMixin
from .actions_candidates import ActionsCandidatesMixin
from .actions_discounts_task_approve import ActionsDiscountsTaskApproveMixin
from .actions_discounts_task_decline import ActionsDiscountsTaskDeclineMixin
from .actions_discounts_task_list import ActionsDiscountsTaskListMixin
from .actions_products import ActionsProductsMixin
from .actions_products_activate import ActionsProductsActivateMixin
from .actions_products_deactivate import ActionsProductsDeactivateMixin


class SellerActionsAPI(
    ActionsMixin,
    ActionsCandidatesMixin,
    ActionsDiscountsTaskApproveMixin,
    ActionsDiscountsTaskDeclineMixin,
    ActionsDiscountsTaskListMixin,
    ActionsProductsMixin,
    ActionsProductsActivateMixin,
    ActionsProductsDeactivateMixin,
):
    """Реализует методы раздела Акции.

    References:
        https://docs.ozon.ru/api/seller/#tag/Promos
    """
    pass
