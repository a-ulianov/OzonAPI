"""Описывает модели методов раздела Работа с грузоместами FBS.
https://docs.ozon.ru/api/seller/#tag/CarriageAPI
"""
__all__ = [
    "ContainerError",
    "PostingError",
    "CarriageContainerCreateRequest",
    "CarriageContainerCreateResponse",
    "CarriageContainerFillRequest",
    "CarriageContainerFillResponse",
    "CarriageContainerApproveRequest",
    "CarriageContainerApproveResponse",
    "CarriageContainerPlaceIntoRequest",
    "CarriageContainerPlaceIntoResponse",
    "CarriageContainerRemovePostingsRequest",
    "CarriageContainerRemovePostingsResponse",
    "CarriageContainerRemoveFromRequest",
    "CarriageContainerRemoveFromResponse",
    "CarriageContainerCancelRequest",
    "CarriageContainerCancelResponse",
    "CarriageContainerListRequest",
    "CarriageContainerListResponse",
    "CarriageContainerListFilter",
    "CarriageContainerListContainer",
    "CarriageContainerGetRequest",
    "CarriageContainerGetResponse",
    "CarriageContainerGetPosting",
    "CarriageContainerGetProduct",
    "CarriageContainerStatusGetRequest",
    "CarriageContainerStatusGetResponse",
    "CarriageContainerStatus",
    "CarriageContainerTaskInfoRequest",
    "CarriageContainerTaskInfoResponse",
    "CarriageContainerDocumentGetRequest",
    "CarriageContainerDocumentGetResponse",
    "CarriageContainerLabelGetRequest",
    "CarriageContainerLabelGetResponse",
    "CarriageContainerLabelGetContent",
]

from .entities import ContainerError, PostingError
from .v1__carriage_container_approve import (
    CarriageContainerApproveRequest,
    CarriageContainerApproveResponse,
)
from .v1__carriage_container_cancel import (
    CarriageContainerCancelRequest,
    CarriageContainerCancelResponse,
)
from .v1__carriage_container_create import (
    CarriageContainerCreateRequest,
    CarriageContainerCreateResponse,
)
from .v1__carriage_container_document_get import (
    CarriageContainerDocumentGetRequest,
    CarriageContainerDocumentGetResponse,
)
from .v1__carriage_container_fill import (
    CarriageContainerFillRequest,
    CarriageContainerFillResponse,
)
from .v1__carriage_container_get import (
    CarriageContainerGetPosting,
    CarriageContainerGetProduct,
    CarriageContainerGetRequest,
    CarriageContainerGetResponse,
)
from .v1__carriage_container_label_get import (
    CarriageContainerLabelGetContent,
    CarriageContainerLabelGetRequest,
    CarriageContainerLabelGetResponse,
)
from .v1__carriage_container_list import (
    CarriageContainerListContainer,
    CarriageContainerListFilter,
    CarriageContainerListRequest,
    CarriageContainerListResponse,
)
from .v1__carriage_container_place_into import (
    CarriageContainerPlaceIntoRequest,
    CarriageContainerPlaceIntoResponse,
)
from .v1__carriage_container_remove_from import (
    CarriageContainerRemoveFromRequest,
    CarriageContainerRemoveFromResponse,
)
from .v1__carriage_container_remove_postings import (
    CarriageContainerRemovePostingsRequest,
    CarriageContainerRemovePostingsResponse,
)
from .v1__carriage_container_status_get import (
    CarriageContainerStatus,
    CarriageContainerStatusGetRequest,
    CarriageContainerStatusGetResponse,
)
from .v1__carriage_container_task_info import (
    CarriageContainerTaskInfoRequest,
    CarriageContainerTaskInfoResponse,
)
