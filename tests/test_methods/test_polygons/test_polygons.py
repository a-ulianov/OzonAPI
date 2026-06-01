import pytest

from src.ozonapi.seller.common.enumerations.polygons import PolygonDeliveryTime
from src.ozonapi.seller.schemas.polygons import (
    PolygonBindRequest,
    PolygonBindResponse,
    PolygonBindV1Polygon,
    PolygonBindV1Request,
    PolygonBindV1Response,
    PolygonBindV1WarehouseLocation,
    PolygonCreateRequest,
    PolygonCreateResponse,
    PolygonDeleteRequest,
    PolygonDeleteResponse,
    PolygonListRequest,
    PolygonListResponse,
    PolygonTimeCoordinatesUpdateRequest,
    PolygonTimeCoordinatesUpdateResponse,
    PolygonTimeSetRequest,
    PolygonTimeSetResponse,
)


class TestPolygonCreate:
    """Тесты для метода polygon_create."""

    @pytest.mark.asyncio
    async def test_polygon_create(self, api, mock_api_request):
        """Тестирует метод polygon_create."""
        mock_api_request.return_value = {"polygon_id": 555}

        request = PolygonCreateRequest(coordinates="[[[58.27,92.13],[58.30,92.16]]]")
        response = await api.polygon_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonCreateResponse)
        assert response.polygon_id == 555


class TestPolygonBind:
    """Тесты для метода polygon_bind (v2)."""

    @pytest.mark.asyncio
    async def test_polygon_bind(self, api, mock_api_request):
        """Тестирует метод polygon_bind."""
        mock_api_request.return_value = {}

        request = PolygonBindRequest(
            delivery_method_id=123,
            polygon_id=456,
            time=PolygonDeliveryTime.MIN_30,
            warehouse_id=789,
        )
        response = await api.polygon_bind(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="polygon/bind",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonBindResponse)


class TestPolygonBindV1:
    """Тесты для метода polygon_bind_v1."""

    @pytest.mark.asyncio
    async def test_polygon_bind_v1(self, api, mock_api_request):
        """Тестирует метод polygon_bind_v1."""
        mock_api_request.return_value = {}

        request = PolygonBindV1Request(
            delivery_method_id=123,
            polygons=[PolygonBindV1Polygon(polygon_id=456, time=30)],
            warehouse_location=PolygonBindV1WarehouseLocation(lat="58.27", lon="92.13"),
        )
        response = await api.polygon_bind_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/bind",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonBindV1Response)


class TestPolygonDelete:
    """Тесты для метода polygon_delete."""

    @pytest.mark.asyncio
    async def test_polygon_delete(self, api, mock_api_request):
        """Тестирует метод polygon_delete."""
        mock_api_request.return_value = {}

        request = PolygonDeleteRequest(
            delivery_method_id=123, polygon_id=456, warehouse_id=789
        )
        response = await api.polygon_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonDeleteResponse)


class TestPolygonList:
    """Тесты для метода polygon_list."""

    @pytest.mark.asyncio
    async def test_polygon_list(self, api, mock_api_request):
        """Тестирует метод polygon_list."""
        mock_api_request.return_value = {
            "polygons": [
                {"polygon_id": 456, "coordinates": "[[[58.27,92.13]]]", "time": 30},
            ]
        }

        request = PolygonListRequest(delivery_method_id=123, warehouse_id=789)
        response = await api.polygon_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonListResponse)
        assert len(response.polygons) == 1
        assert response.polygons[0].polygon_id == 456
        assert response.polygons[0].time == 30


class TestPolygonTimeCoordinatesUpdate:
    """Тесты для метода polygon_time_coordinates_update."""

    @pytest.mark.asyncio
    async def test_polygon_time_coordinates_update(self, api, mock_api_request):
        """Тестирует метод polygon_time_coordinates_update."""
        mock_api_request.return_value = {}

        request = PolygonTimeCoordinatesUpdateRequest(
            coordinates="[[[58.27,92.13],[58.30,92.16]]]",
            delivery_method_id=123,
            polygon_id=456,
            warehouse_id=789,
        )
        response = await api.polygon_time_coordinates_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/time/coordinates/update",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonTimeCoordinatesUpdateResponse)


class TestPolygonTimeSet:
    """Тесты для метода polygon_time_set."""

    @pytest.mark.asyncio
    async def test_polygon_time_set(self, api, mock_api_request):
        """Тестирует метод polygon_time_set."""
        mock_api_request.return_value = {}

        request = PolygonTimeSetRequest(
            current_time=PolygonDeliveryTime.MIN_30,
            new_time=PolygonDeliveryTime.MIN_60,
            delivery_method_id=123,
            polygon_id=456,
            warehouse_id=789,
        )
        response = await api.polygon_time_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="polygon/time/set",
            payload=request.model_dump(),
        )
        assert isinstance(response, PolygonTimeSetResponse)
