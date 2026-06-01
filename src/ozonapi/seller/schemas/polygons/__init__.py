"""Описывает модели раздела «Полигоны».
https://docs.ozon.ru/api/seller/#tag/PolygonAPI
"""
__all__ = [
    "PolygonCreateRequest",
    "PolygonCreateResponse",
    "PolygonBindRequest",
    "PolygonBindResponse",
    "PolygonBindV1Request",
    "PolygonBindV1Response",
    "PolygonBindV1Polygon",
    "PolygonBindV1WarehouseLocation",
    "PolygonDeleteRequest",
    "PolygonDeleteResponse",
    "PolygonListRequest",
    "PolygonListResponse",
    "PolygonListPolygon",
    "PolygonTimeCoordinatesUpdateRequest",
    "PolygonTimeCoordinatesUpdateResponse",
    "PolygonTimeSetRequest",
    "PolygonTimeSetResponse",
]

from .v1__polygon_create import (
    PolygonCreateRequest,
    PolygonCreateResponse,
)
from .v1__polygon_bind import (
    PolygonBindV1Polygon,
    PolygonBindV1Request,
    PolygonBindV1Response,
    PolygonBindV1WarehouseLocation,
)
from .v2__polygon_bind import (
    PolygonBindRequest,
    PolygonBindResponse,
)
from .v1__polygon_delete import (
    PolygonDeleteRequest,
    PolygonDeleteResponse,
)
from .v1__polygon_list import (
    PolygonListPolygon,
    PolygonListRequest,
    PolygonListResponse,
)
from .v1__polygon_time_coordinates_update import (
    PolygonTimeCoordinatesUpdateRequest,
    PolygonTimeCoordinatesUpdateResponse,
)
from .v1__polygon_time_set import (
    PolygonTimeSetRequest,
    PolygonTimeSetResponse,
)
