"""Композиция миксинов методов раздела заявок на поставку FBO.

Объединяет методы создания и управления заявками на поставку FBO в единый класс
:class:`SellerFboSupplyRequestAPI`.
"""

from ...core import APIManager
from .cargoes_create import CargoesCreateMixin
from .cargoes_create_info import CargoesCreateInfoMixin
from .cargoes_delete import CargoesDeleteMixin
from .cargoes_delete_status import CargoesDeleteStatusMixin
from .cargoes_delete_status_v1 import CargoesDeleteStatusV1Mixin
from .cargoes_delete_v1 import CargoesDeleteV1Mixin
from .cargoes_get import CargoesGetMixin
from .cargoes_get_v1 import CargoesGetV1Mixin
from .cargoes_label_create import CargoesLabelCreateMixin
from .cargoes_label_file import CargoesLabelFileMixin
from .cargoes_label_get import CargoesLabelGetMixin
from .cargoes_label_transport_by_order_create import (
    CargoesLabelTransportByOrderCreateMixin,
)
from .cargoes_label_transport_by_order_status import (
    CargoesLabelTransportByOrderStatusMixin,
)
from .cargoes_label_transport_create import CargoesLabelTransportCreateMixin
from .cargoes_label_transport_status import CargoesLabelTransportStatusMixin
from .cargoes_rules_get import CargoesRulesGetMixin
from .cargoes_supplies_get import CargoesSuppliesGetMixin
from .cargoes_transport_activate import CargoesTransportActivateMixin
from .cargoes_transport_activate_status import (
    CargoesTransportActivateStatusMixin,
)
from .cargoes_transport_bind import CargoesTransportBindMixin
from .cargoes_transport_bind_status import CargoesTransportBindStatusMixin
from .cargoes_transport_create import CargoesTransportCreateMixin
from .cargoes_transport_create_status import CargoesTransportCreateStatusMixin
from .cluster_list_v1 import ClusterListV1Mixin
from .draft_create import DraftCreateMixin
from .draft_create_info import DraftCreateInfoMixin
from .draft_create_info_v1 import DraftCreateInfoV1Mixin
from .draft_crossdock_create import DraftCrossdockCreateMixin
from .draft_direct_create import DraftDirectCreateMixin
from .draft_multi_cluster_create import DraftMultiClusterCreateMixin
from .draft_supply_create import DraftSupplyCreateMixin
from .draft_supply_create_status import DraftSupplyCreateStatusMixin
from .draft_supply_create_status_v1 import DraftSupplyCreateStatusV1Mixin
from .draft_supply_create_v1 import DraftSupplyCreateV1Mixin
from .draft_timeslot_info import DraftTimeslotInfoMixin
from .draft_timeslot_info_v1 import DraftTimeslotInfoV1Mixin
from .supply_order_cancel import SupplyOrderCancelMixin
from .supply_order_cancel_status import SupplyOrderCancelStatusMixin
from .supply_order_content_update import SupplyOrderContentUpdateMixin
from .supply_order_content_update_status import (
    SupplyOrderContentUpdateStatusMixin,
)
from .supply_order_content_update_validation import (
    SupplyOrderContentUpdateValidationMixin,
)
from .warehouse_fbo_list import WarehouseFboListMixin
from .warehouse_fbo_seller_list import WarehouseFboSellerListMixin


class SellerFboSupplyRequestAPI(
    CargoesCreateMixin,
    CargoesCreateInfoMixin,
    CargoesDeleteMixin,
    CargoesDeleteStatusMixin,
    CargoesDeleteStatusV1Mixin,
    CargoesDeleteV1Mixin,
    CargoesGetMixin,
    CargoesGetV1Mixin,
    CargoesLabelCreateMixin,
    CargoesLabelFileMixin,
    CargoesLabelGetMixin,
    CargoesLabelTransportByOrderCreateMixin,
    CargoesLabelTransportByOrderStatusMixin,
    CargoesLabelTransportCreateMixin,
    CargoesLabelTransportStatusMixin,
    CargoesRulesGetMixin,
    CargoesSuppliesGetMixin,
    CargoesTransportActivateMixin,
    CargoesTransportActivateStatusMixin,
    CargoesTransportBindMixin,
    CargoesTransportBindStatusMixin,
    CargoesTransportCreateMixin,
    CargoesTransportCreateStatusMixin,
    ClusterListV1Mixin,
    DraftCreateMixin,
    DraftCreateInfoMixin,
    DraftCreateInfoV1Mixin,
    DraftCrossdockCreateMixin,
    DraftDirectCreateMixin,
    DraftMultiClusterCreateMixin,
    DraftSupplyCreateMixin,
    DraftSupplyCreateStatusMixin,
    DraftSupplyCreateStatusV1Mixin,
    DraftSupplyCreateV1Mixin,
    DraftTimeslotInfoMixin,
    DraftTimeslotInfoV1Mixin,
    SupplyOrderCancelMixin,
    SupplyOrderCancelStatusMixin,
    SupplyOrderContentUpdateMixin,
    SupplyOrderContentUpdateStatusMixin,
    SupplyOrderContentUpdateValidationMixin,
    WarehouseFboListMixin,
    WarehouseFboSellerListMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела заявок на поставку FBO.

    Notes:
        • Справочные методы (кластеры, склады отгрузки), создание черновика заявки
          на поставку, получение информации о черновике и доступных таймслотов.

    References:
        • https://docs.ozon.ru/api/seller/#tag/FboSupplyRequestAPI
    """

    pass
