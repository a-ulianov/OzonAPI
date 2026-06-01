import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpDraftDropOffCreateDeliveryDetails,
    FbpDraftDropOffCreateRequest,
    FbpDraftDropOffCreateResponse,
    FbpDraftDropOffDeleteRequest,
    FbpDraftDropOffDeleteResponse,
    FbpDraftDropOffDlvEditRequest,
    FbpDraftDropOffDlvEditResponse,
    FbpDraftDropOffPointListRequest,
    FbpDraftDropOffPointListResponse,
    FbpDraftDropOffPointTimetableRequest,
    FbpDraftDropOffPointTimetableResponse,
    FbpDraftDropOffProductValidateRequest,
    FbpDraftDropOffProductValidateResponse,
    FbpDraftDropOffProvinceListRequest,
    FbpDraftDropOffProvinceListResponse,
    FbpDraftDropOffRegistrateRequest,
    FbpDraftDropOffRegistrateResponse,
    FbpProductValidateSkuItem,
)


class TestFbpDraftDropOffCreate:
    """Тесты для метода fbp_draft_drop_off_create."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_create(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_create."""
        mock_api_request.return_value = {"draft_id": 20, "supply_id": "60", "row_version": 1}

        request = FbpDraftDropOffCreateRequest(
            bundle_id="b1",
            delivery_details=FbpDraftDropOffCreateDeliveryDetails(
                drop_off_date="2026-06-10T10:00:00Z",
                drop_off_point_id=7,
                drop_off_province_uuid="uuid-1",
            ),
            package_units_count=1,
            warehouse_id=123,
        )
        response = await api.fbp_draft_drop_off_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffCreateResponse)
        assert response.draft_id == 20


class TestFbpDraftDropOffDelete:
    """Тесты для метода fbp_draft_drop_off_delete."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_delete(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_delete."""
        mock_api_request.return_value = {
            "cancellation_state": {"cancellation_status": "CANCELED"},
            "row_version": 2,
        }

        request = FbpDraftDropOffDeleteRequest(supply_id="60")
        response = await api.fbp_draft_drop_off_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffDeleteResponse)
        assert response.cancellation_state.cancellation_status == "CANCELED"


class TestFbpDraftDropOffDlvEdit:
    """Тесты для метода fbp_draft_drop_off_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_dlv_edit."""
        mock_api_request.return_value = {"row_version": 3}

        request = FbpDraftDropOffDlvEditRequest(
            supply_id="60",
            row_version=2,
            drop_off_date="2026-06-11T10:00:00Z",
            drop_off_point_id=7,
            drop_off_province_uuid="uuid-1",
        )
        response = await api.fbp_draft_drop_off_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffDlvEditResponse)
        assert response.row_version == 3


class TestFbpDraftDropOffRegistrate:
    """Тесты для метода fbp_draft_drop_off_registrate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_registrate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_registrate."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {
                "order_error": "DROP_OFF_POINTS_IS_EMPTY",
                "bundle_errors": [{"sku": 123, "errors": ["NO_PRICE"]}],
            },
            "row_version": 2,
        }

        request = FbpDraftDropOffRegistrateRequest(supply_id="60", row_version=1)
        response = await api.fbp_draft_drop_off_registrate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/registrate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffRegistrateResponse)
        assert response.error.order_error == "DROP_OFF_POINTS_IS_EMPTY"
        assert response.error.bundle_errors[0].sku == 123


class TestFbpDraftDropOffProvinceList:
    """Тесты для метода fbp_draft_drop_off_province_list."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_province_list(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_province_list."""
        mock_api_request.return_value = {
            "provinces": [
                {"province_uuid": "uuid-1", "name": "Москва", "points_count": 5}
            ]
        }

        request = FbpDraftDropOffProvinceListRequest(warehouse_id=123)
        response = await api.fbp_draft_drop_off_province_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/province/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffProvinceListResponse)
        assert response.provinces[0].name == "Москва"
        assert response.provinces[0].points_count == 5


class TestFbpDraftDropOffPointList:
    """Тесты для метода fbp_draft_drop_off_point_list."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_point_list(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_point_list."""
        mock_api_request.return_value = {
            "drop_off_points": [
                {
                    "drop_off_point_id": 7,
                    "province_uuid": "uuid-1",
                    "city": "Москва",
                    "point_address": "ул. Тестовая, 1",
                    "nearest_drop_off_date": "2026-06-10T10:00:00Z",
                }
            ]
        }

        request = FbpDraftDropOffPointListRequest(
            warehouse_id=123, province_uuid="uuid-1", page_size=50
        )
        response = await api.fbp_draft_drop_off_point_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/point/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffPointListResponse)
        assert response.drop_off_points[0].drop_off_point_id == 7
        assert response.drop_off_points[0].city == "Москва"


class TestFbpDraftDropOffPointTimetable:
    """Тесты для метода fbp_draft_drop_off_point_timetable."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_point_timetable(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_point_timetable."""
        mock_api_request.return_value = {
            "calendar": [
                {
                    "day_of_week": "MONDAY",
                    "calendar_item": {
                        "opening_hours": {"timeslot_start": "09:00", "timeslot_end": "18:00"},
                        "break_hours": {"timeslot_start": "13:00", "timeslot_end": "14:00"},
                        "is_holiday": False,
                    },
                }
            ]
        }

        request = FbpDraftDropOffPointTimetableRequest(
            warehouse_id=123, province_uuid="uuid-1", drop_off_point_id=7
        )
        response = await api.fbp_draft_drop_off_point_timetable(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/point/timetable",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffPointTimetableResponse)
        assert response.calendar[0].day_of_week == "MONDAY"
        assert response.calendar[0].calendar_item.opening_hours.timeslot_start == "09:00"
        assert response.calendar[0].calendar_item.is_holiday is False


class TestFbpDraftDropOffProductValidate:
    """Тесты для метода fbp_draft_drop_off_product_validate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_drop_off_product_validate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_drop_off_product_validate."""
        mock_api_request.return_value = {
            "bundle_generated": True,
            "bundle_id": "bundle-2",
            "approved_items": [{"sku": 123, "name": "Товар", "quantity": 1}],
            "rejected_items": [{"sku": 456, "rejection_reasons": ["BANNED"]}],
        }

        request = FbpDraftDropOffProductValidateRequest(
            skus=[FbpProductValidateSkuItem(sku=123, count=1)],
            warehouse_id=123,
        )
        response = await api.fbp_draft_drop_off_product_validate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/product/validate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDropOffProductValidateResponse)
        assert response.bundle_id == "bundle-2"
        assert response.approved_items[0].sku == 123
        assert response.rejected_items[0].rejection_reasons == ["BANNED"]
