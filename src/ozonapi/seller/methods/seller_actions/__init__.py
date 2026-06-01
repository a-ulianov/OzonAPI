__all__ = ["SellerSellerActionsAPI", ]

from .seller_actions_archive import SellerActionsArchiveMixin
from .seller_actions_change_activity import SellerActionsChangeActivityMixin
from .seller_actions_create_discount import SellerActionsCreateDiscountMixin
from .seller_actions_create_discount_with_condition import (
    SellerActionsCreateDiscountWithConditionMixin,
)
from .seller_actions_create_installment import SellerActionsCreateInstallmentMixin
from .seller_actions_create_multi_level_discount import (
    SellerActionsCreateMultiLevelDiscountMixin,
)
from .seller_actions_create_voucher import SellerActionsCreateVoucherMixin
from .seller_actions_list import SellerActionsListMixin
from .seller_actions_products_add import SellerActionsProductsAddMixin
from .seller_actions_products_candidates import SellerActionsProductsCandidatesMixin
from .seller_actions_products_delete import SellerActionsProductsDeleteMixin
from .seller_actions_products_list import SellerActionsProductsListMixin
from .seller_actions_update_discount import SellerActionsUpdateDiscountMixin
from .seller_actions_update_discount_with_condition import (
    SellerActionsUpdateDiscountWithConditionMixin,
)
from .seller_actions_update_installment import SellerActionsUpdateInstallmentMixin
from .seller_actions_update_multi_level_discount import (
    SellerActionsUpdateMultiLevelDiscountMixin,
)
from .seller_actions_update_voucher import SellerActionsUpdateVoucherMixin
from .seller_actions_voucher_get import SellerActionsVoucherGetMixin


class SellerSellerActionsAPI(
    SellerActionsArchiveMixin,
    SellerActionsChangeActivityMixin,
    SellerActionsCreateDiscountMixin,
    SellerActionsCreateDiscountWithConditionMixin,
    SellerActionsCreateInstallmentMixin,
    SellerActionsCreateMultiLevelDiscountMixin,
    SellerActionsCreateVoucherMixin,
    SellerActionsListMixin,
    SellerActionsProductsAddMixin,
    SellerActionsProductsCandidatesMixin,
    SellerActionsProductsDeleteMixin,
    SellerActionsProductsListMixin,
    SellerActionsUpdateDiscountMixin,
    SellerActionsUpdateDiscountWithConditionMixin,
    SellerActionsUpdateInstallmentMixin,
    SellerActionsUpdateMultiLevelDiscountMixin,
    SellerActionsUpdateVoucherMixin,
    SellerActionsVoucherGetMixin,
):
    """Реализует методы раздела «Акции продавца».

    References:
        https://docs.ozon.ru/api/seller/#tag/SellerActions
    """
    pass
