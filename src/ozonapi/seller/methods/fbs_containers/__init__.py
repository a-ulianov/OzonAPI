"""Композиция миксинов методов раздела Работа с грузоместами FBS (beta).

Объединяет методы работы с грузоместами FBS (carriage/container)
в единый класс :class:`SellerFBSContainerAPI`.
"""

from ...core import APIManager
from .carriage_container_approve import CarriageContainerApproveMixin
from .carriage_container_cancel import CarriageContainerCancelMixin
from .carriage_container_create import CarriageContainerCreateMixin
from .carriage_container_document_get import CarriageContainerDocumentGetMixin
from .carriage_container_fill import CarriageContainerFillMixin
from .carriage_container_get import CarriageContainerGetMixin
from .carriage_container_label_get import CarriageContainerLabelGetMixin
from .carriage_container_list import CarriageContainerListMixin
from .carriage_container_place_into import CarriageContainerPlaceIntoMixin
from .carriage_container_remove_from import CarriageContainerRemoveFromMixin
from .carriage_container_remove_postings import CarriageContainerRemovePostingsMixin
from .carriage_container_status_get import CarriageContainerStatusGetMixin
from .carriage_container_task_info import CarriageContainerTaskInfoMixin


class SellerFBSContainerAPI(
    CarriageContainerApproveMixin,
    CarriageContainerCancelMixin,
    CarriageContainerCreateMixin,
    CarriageContainerDocumentGetMixin,
    CarriageContainerFillMixin,
    CarriageContainerGetMixin,
    CarriageContainerLabelGetMixin,
    CarriageContainerListMixin,
    CarriageContainerPlaceIntoMixin,
    CarriageContainerRemoveFromMixin,
    CarriageContainerRemovePostingsMixin,
    CarriageContainerStatusGetMixin,
    CarriageContainerTaskInfoMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Работа с грузоместами FBS (beta).

    Notes:
        • Объединяет методы создания, наполнения, подтверждения, размещения и отмены
          грузомест, а также получения списков, статусов, документов и этикеток.

    References:
        • https://docs.ozon.ru/api/seller/#tag/CarriageAPI
    """

    pass
