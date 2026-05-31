"""Описывает модели методов раздела Возвраты.
https://docs.ozon.ru/api/seller/#tag/ReturnsAPI
"""
__all__ = [
    "ReturnsMoney",
    "ReturnsTimeRange",
    "ReturnsPlace",
    "ReturnsStatus",
    "ReturnsListRequest",
    "ReturnsListResponse",
    "ReturnsListFilter",
    "ReturnsListItem",
    "ReturnsListExemplar",
    "ReturnsListStorage",
    "ReturnsListProduct",
    "ReturnsListLogistic",
    "ReturnsListVisual",
    "ReturnsListAdditionalInfo",
    "ReturnsListCompensation",
    "ReturnsSettingsUtilizationHistoryResponse",
    "ReturnsSettingsUtilizationHistoryItem",
    "ReturnsSettingsUtilizationInfoResponse",
    "ReturnsSettingsUtilizationInfoSettings",
    "UtilizationMoney",
    "ReturnsSettingsUtilizationUpdateRequest",
    "ReturnsSettingsUtilizationUpdateResponse",
    "ReturnsSettingsUtilizationUpdatePrice",
    "ReturnsRfbsProduct",
    "ReturnsRfbsListRequest",
    "ReturnsRfbsListResponse",
    "ReturnsRfbsListFilter",
    "ReturnsRfbsCreatedAt",
    "ReturnsRfbsListItem",
    "ReturnsRfbsListState",
    "ReturnsRfbsGetRequest",
    "ReturnsRfbsGetResponse",
    "ReturnsRfbsGetReturn",
    "ReturnsRfbsGetAvailableAction",
    "ReturnsRfbsGetClientReturnMethodType",
    "ReturnsRfbsGetRejectionReason",
    "ReturnsRfbsGetReturnReason",
    "ReturnsRfbsGetState",
    "ReturnsRfbsRejectRequest",
    "ReturnsRfbsRejectResponse",
    "ReturnsRfbsCompensateRequest",
    "ReturnsRfbsCompensateResponse",
    "ReturnsRfbsVerifyRequest",
    "ReturnsRfbsVerifyResponse",
    "ReturnsRfbsReceiveReturnRequest",
    "ReturnsRfbsReceiveReturnResponse",
    "ReturnsRfbsReturnMoneyRequest",
    "ReturnsRfbsReturnMoneyResponse",
    "ReturnsRfbsActionSetRequest",
    "ReturnsRfbsActionSetResponse",
    "ReturnsCompanyFbsInfoRequest",
    "ReturnsCompanyFbsInfoResponse",
    "ReturnsCompanyFbsInfoFilter",
    "ReturnsCompanyFbsInfoPagination",
    "ReturnsCompanyFbsInfoDropOffPoint",
    "ReturnsCompanyFbsInfoPassInfo",
    "ReturnGiveoutIsEnabledResponse",
    "ReturnGiveoutListRequest",
    "ReturnGiveoutListResponse",
    "ReturnGiveoutListItem",
    "ReturnGiveoutInfoRequest",
    "ReturnGiveoutInfoResponse",
    "ReturnGiveoutInfoArticle",
    "ReturnGiveoutBarcodeResponse",
    "ReturnGiveoutGetPDFResponse",
    "ReturnGiveoutGetPNGResponse",
    "ReturnGiveoutBarcodeResetResponse",
]

from .entities import (
    ReturnsMoney,
    ReturnsPlace,
    ReturnsRfbsProduct,
    ReturnsStatus,
    ReturnsTimeRange,
)
from .v1__return_giveout_barcode import ReturnGiveoutBarcodeResponse
from .v1__return_giveout_barcode_reset import ReturnGiveoutBarcodeResetResponse
from .v1__return_giveout_get_pdf import ReturnGiveoutGetPDFResponse
from .v1__return_giveout_get_png import ReturnGiveoutGetPNGResponse
from .v1__return_giveout_info import (
    ReturnGiveoutInfoArticle,
    ReturnGiveoutInfoRequest,
    ReturnGiveoutInfoResponse,
)
from .v1__return_giveout_is_enabled import ReturnGiveoutIsEnabledResponse
from .v1__return_giveout_list import (
    ReturnGiveoutListItem,
    ReturnGiveoutListRequest,
    ReturnGiveoutListResponse,
)
from .v1__returns_company_fbs_info import (
    ReturnsCompanyFbsInfoDropOffPoint,
    ReturnsCompanyFbsInfoFilter,
    ReturnsCompanyFbsInfoPagination,
    ReturnsCompanyFbsInfoPassInfo,
    ReturnsCompanyFbsInfoRequest,
    ReturnsCompanyFbsInfoResponse,
)
from .v1__returns_list import (
    ReturnsListAdditionalInfo,
    ReturnsListCompensation,
    ReturnsListExemplar,
    ReturnsListFilter,
    ReturnsListItem,
    ReturnsListLogistic,
    ReturnsListProduct,
    ReturnsListRequest,
    ReturnsListResponse,
    ReturnsListStorage,
    ReturnsListVisual,
)
from .v1__returns_rfbs_action_set import (
    ReturnsRfbsActionSetRequest,
    ReturnsRfbsActionSetResponse,
)
from .v1__returns_settings_utilization_history import (
    ReturnsSettingsUtilizationHistoryItem,
    ReturnsSettingsUtilizationHistoryResponse,
)
from .v1__returns_settings_utilization_info import (
    ReturnsSettingsUtilizationInfoResponse,
    ReturnsSettingsUtilizationInfoSettings,
    UtilizationMoney,
)
from .v1__returns_settings_utilization_update import (
    ReturnsSettingsUtilizationUpdatePrice,
    ReturnsSettingsUtilizationUpdateRequest,
    ReturnsSettingsUtilizationUpdateResponse,
)
from .v2__returns_rfbs_compensate import (
    ReturnsRfbsCompensateRequest,
    ReturnsRfbsCompensateResponse,
)
from .v2__returns_rfbs_get import (
    ReturnsRfbsGetAvailableAction,
    ReturnsRfbsGetClientReturnMethodType,
    ReturnsRfbsGetRejectionReason,
    ReturnsRfbsGetRequest,
    ReturnsRfbsGetResponse,
    ReturnsRfbsGetReturn,
    ReturnsRfbsGetReturnReason,
    ReturnsRfbsGetState,
)
from .v2__returns_rfbs_list import (
    ReturnsRfbsCreatedAt,
    ReturnsRfbsListFilter,
    ReturnsRfbsListItem,
    ReturnsRfbsListRequest,
    ReturnsRfbsListResponse,
    ReturnsRfbsListState,
)
from .v2__returns_rfbs_receive_return import (
    ReturnsRfbsReceiveReturnRequest,
    ReturnsRfbsReceiveReturnResponse,
)
from .v2__returns_rfbs_reject import (
    ReturnsRfbsRejectRequest,
    ReturnsRfbsRejectResponse,
)
from .v2__returns_rfbs_return_money import (
    ReturnsRfbsReturnMoneyRequest,
    ReturnsRfbsReturnMoneyResponse,
)
from .v2__returns_rfbs_verify import (
    ReturnsRfbsVerifyRequest,
    ReturnsRfbsVerifyResponse,
)
