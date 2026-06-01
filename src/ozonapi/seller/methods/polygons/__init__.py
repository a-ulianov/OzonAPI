__all__ = ["SellerPolygonAPI", ]

from .polygon_create import PolygonCreateMixin
from .polygon_bind import PolygonBindMixin
from .polygon_bind_v1 import PolygonBindV1Mixin
from .polygon_delete import PolygonDeleteMixin
from .polygon_list import PolygonListMixin
from .polygon_time_coordinates_update import PolygonTimeCoordinatesUpdateMixin
from .polygon_time_set import PolygonTimeSetMixin


class SellerPolygonAPI(
    PolygonCreateMixin,
    PolygonBindMixin,
    PolygonBindV1Mixin,
    PolygonDeleteMixin,
    PolygonListMixin,
    PolygonTimeCoordinatesUpdateMixin,
    PolygonTimeSetMixin,
):
    """Реализует методы раздела «Полигоны».

    References:
        https://docs.ozon.ru/api/seller/#tag/PolygonAPI
    """
    pass
