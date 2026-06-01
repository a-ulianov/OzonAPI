"""Описывает модели методов раздела «Акции продавца».
https://docs.ozon.ru/api/seller/#tag/SellerActions
"""
__all__ = [
    "SellerActionDiscountLevel",
    "SellerActionProduct",
    "SellerActionsCreateDiscountRequest",
    "SellerActionsCreateDiscountResponse",
    "SellerActionsCreateDiscountWithConditionRequest",
    "SellerActionsCreateDiscountWithConditionResponse",
    "SellerActionsCreateInstallmentRequest",
    "SellerActionsCreateInstallmentResponse",
    "SellerActionsCreateMultiLevelDiscountRequest",
    "SellerActionsCreateMultiLevelDiscountResponse",
    "SellerActionsCreateVoucherParameter",
    "SellerActionsCreateVoucherRequest",
    "SellerActionsCreateVoucherResponse",
    "SellerActionsUpdateDiscountParameters",
    "SellerActionsUpdateDiscountRequest",
    "SellerActionsUpdateDiscountResponse",
    "SellerActionsUpdateDiscountWithConditionParameters",
    "SellerActionsUpdateDiscountWithConditionRequest",
    "SellerActionsUpdateDiscountWithConditionResponse",
    "SellerActionsUpdateInstallmentParameters",
    "SellerActionsUpdateInstallmentRequest",
    "SellerActionsUpdateInstallmentResponse",
    "SellerActionsUpdateMultiLevelDiscountParameters",
    "SellerActionsUpdateMultiLevelDiscountRequest",
    "SellerActionsUpdateMultiLevelDiscountResponse",
    "SellerActionsUpdateVoucherParameters",
    "SellerActionsUpdateVoucherRequest",
    "SellerActionsUpdateVoucherResponse",
    "SellerActionsProductsAddProduct",
    "SellerActionsProductsAddRequest",
    "SellerActionsProductsAddResponse",
    "SellerActionsProductsCandidatesRequest",
    "SellerActionsProductsCandidatesResponse",
    "SellerActionsProductsDeleteRequest",
    "SellerActionsProductsDeleteResponse",
    "SellerActionsProductsListRequest",
    "SellerActionsProductsListResponse",
    "SellerActionsArchiveRequest",
    "SellerActionsArchiveResponse",
    "SellerActionsChangeActivityRequest",
    "SellerActionsChangeActivityResponse",
    "SellerActionsListRequest",
    "SellerActionsListResponse",
    "SellerActionsListAction",
    "SellerActionsListParameters",
    "SellerActionsListVoucherParameter",
    "SellerActionsListPickedSegment",
    "SellerActionsListSegment",
    "SellerActionsVoucherGetRequest",
    "SellerActionsVoucherGetResponse",
]

from .base import (
    SellerActionDiscountLevel,
    SellerActionProduct,
)
from .v1__seller_actions_create_discount import (
    SellerActionsCreateDiscountRequest,
    SellerActionsCreateDiscountResponse,
)
from .v1__seller_actions_create_discount_with_condition import (
    SellerActionsCreateDiscountWithConditionRequest,
    SellerActionsCreateDiscountWithConditionResponse,
)
from .v1__seller_actions_create_installment import (
    SellerActionsCreateInstallmentRequest,
    SellerActionsCreateInstallmentResponse,
)
from .v1__seller_actions_create_multi_level_discount import (
    SellerActionsCreateMultiLevelDiscountRequest,
    SellerActionsCreateMultiLevelDiscountResponse,
)
from .v1__seller_actions_create_voucher import (
    SellerActionsCreateVoucherParameter,
    SellerActionsCreateVoucherRequest,
    SellerActionsCreateVoucherResponse,
)
from .v1__seller_actions_update_discount import (
    SellerActionsUpdateDiscountParameters,
    SellerActionsUpdateDiscountRequest,
    SellerActionsUpdateDiscountResponse,
)
from .v1__seller_actions_update_discount_with_condition import (
    SellerActionsUpdateDiscountWithConditionParameters,
    SellerActionsUpdateDiscountWithConditionRequest,
    SellerActionsUpdateDiscountWithConditionResponse,
)
from .v1__seller_actions_update_installment import (
    SellerActionsUpdateInstallmentParameters,
    SellerActionsUpdateInstallmentRequest,
    SellerActionsUpdateInstallmentResponse,
)
from .v1__seller_actions_update_multi_level_discount import (
    SellerActionsUpdateMultiLevelDiscountParameters,
    SellerActionsUpdateMultiLevelDiscountRequest,
    SellerActionsUpdateMultiLevelDiscountResponse,
)
from .v1__seller_actions_update_voucher import (
    SellerActionsUpdateVoucherParameters,
    SellerActionsUpdateVoucherRequest,
    SellerActionsUpdateVoucherResponse,
)
from .v1__seller_actions_products_add import (
    SellerActionsProductsAddProduct,
    SellerActionsProductsAddRequest,
    SellerActionsProductsAddResponse,
)
from .v1__seller_actions_products_candidates import (
    SellerActionsProductsCandidatesRequest,
    SellerActionsProductsCandidatesResponse,
)
from .v1__seller_actions_products_delete import (
    SellerActionsProductsDeleteRequest,
    SellerActionsProductsDeleteResponse,
)
from .v1__seller_actions_products_list import (
    SellerActionsProductsListRequest,
    SellerActionsProductsListResponse,
)
from .v1__seller_actions_archive import (
    SellerActionsArchiveRequest,
    SellerActionsArchiveResponse,
)
from .v1__seller_actions_change_activity import (
    SellerActionsChangeActivityRequest,
    SellerActionsChangeActivityResponse,
)
from .v1__seller_actions_list import (
    SellerActionsListAction,
    SellerActionsListParameters,
    SellerActionsListPickedSegment,
    SellerActionsListRequest,
    SellerActionsListResponse,
    SellerActionsListSegment,
    SellerActionsListVoucherParameter,
)
from .v1__seller_actions_voucher_get import (
    SellerActionsVoucherGetRequest,
    SellerActionsVoucherGetResponse,
)
