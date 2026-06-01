"""Описывает модели методов раздела Пропуски.
https://docs.ozon.ru/api/seller/#tag/Pass
"""
__all__ = [
    "ArrivalPassDriverVehicle",
    "CarriagePassCreateArrivalPass",
    "CarriagePassCreateRequest",
    "CarriagePassCreateResponse",
    "CarriagePassDeleteRequest",
    "CarriagePassDeleteResponse",
    "CarriagePassUpdateArrivalPass",
    "CarriagePassUpdateRequest",
    "CarriagePassUpdateResponse",
    "PassListArrivalPass",
    "PassListFilter",
    "PassListRequest",
    "PassListResponse",
    "ReturnPassCreateArrivalPass",
    "ReturnPassCreateRequest",
    "ReturnPassCreateResponse",
    "ReturnPassDeleteRequest",
    "ReturnPassDeleteResponse",
    "ReturnPassUpdateArrivalPass",
    "ReturnPassUpdateRequest",
    "ReturnPassUpdateResponse",
]

from .entities import ArrivalPassDriverVehicle
from .v1__carriage_pass_create import (
    CarriagePassCreateArrivalPass,
    CarriagePassCreateRequest,
    CarriagePassCreateResponse,
)
from .v1__carriage_pass_delete import (
    CarriagePassDeleteRequest,
    CarriagePassDeleteResponse,
)
from .v1__carriage_pass_update import (
    CarriagePassUpdateArrivalPass,
    CarriagePassUpdateRequest,
    CarriagePassUpdateResponse,
)
from .v1__pass_list import (
    PassListArrivalPass,
    PassListFilter,
    PassListRequest,
    PassListResponse,
)
from .v1__return_pass_create import (
    ReturnPassCreateArrivalPass,
    ReturnPassCreateRequest,
    ReturnPassCreateResponse,
)
from .v1__return_pass_delete import (
    ReturnPassDeleteRequest,
    ReturnPassDeleteResponse,
)
from .v1__return_pass_update import (
    ReturnPassUpdateArrivalPass,
    ReturnPassUpdateRequest,
    ReturnPassUpdateResponse,
)
