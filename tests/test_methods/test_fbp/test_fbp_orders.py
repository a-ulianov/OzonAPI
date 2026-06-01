import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpOrderDirectCancelRequest,
    FbpOrderDirectCancelResponse,
    FbpOrderDirectSellerDlvEditRequest,
    FbpOrderDirectSellerDlvEditResponse,
    FbpOrderDirectTimeslotEditRequest,
    FbpOrderDirectTimeslotEditResponse,
    FbpOrderDirectTimeslotListRequest,
    FbpOrderDirectTimeslotListResponse,
    FbpOrderDropOffCancelRequest,
    FbpOrderDropOffCancelResponse,
    FbpOrderDropOffDlvEditRequest,
    FbpOrderDropOffDlvEditResponse,
    FbpOrderDropOffTimetableRequest,
    FbpOrderDropOffTimetableResponse,
    FbpOrderPickUpCancelRequest,
    FbpOrderPickUpCancelResponse,
    FbpOrderPickUpDlvEditRequest,
    FbpOrderPickUpDlvEditResponse,
    FbpOrderPickUpEditDetails,
)


class TestFbpOrderDirectCancel:
    """Тесты для метода fbp_order_direct_cancel."""

    @pytest.mark.asyncio
    async def test_fbp_order_direct_cancel(self, api, mock_api_request):
        """Тестирует метод fbp_order_direct_cancel."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {"order_errors": ["ORDER_LOCKED"]},
            "row_version": 2,
        }

        request = FbpOrderDirectCancelRequest(supply_id="70")
        response = await api.fbp_order_direct_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/cancel",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDirectCancelResponse)
        assert response.is_error is True
        assert response.error.order_errors == ["ORDER_LOCKED"]


class TestFbpOrderDirectSellerDlvEdit:
    """Тесты для метода fbp_order_direct_seller_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_order_direct_seller_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_order_direct_seller_dlv_edit."""
        mock_api_request.return_value = {"is_error": False, "row_version": 3}

        request = FbpOrderDirectSellerDlvEditRequest(
            supply_id="70",
            row_version=2,
            driver_name="Иванов",
            vehicle_number="А123ВС777",
            vehicle_type="Грузовой",
        )
        response = await api.fbp_order_direct_seller_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/seller-dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDirectSellerDlvEditResponse)
        assert response.is_error is False


class TestFbpOrderDirectTimeslotEdit:
    """Тесты для метода fbp_order_direct_timeslot_edit."""

    @pytest.mark.asyncio
    async def test_fbp_order_direct_timeslot_edit(self, api, mock_api_request):
        """Тестирует метод fbp_order_direct_timeslot_edit."""
        mock_api_request.return_value = {"error_reasons": ["LOGISTICS_REASON"], "row_version": 3}

        request = FbpOrderDirectTimeslotEditRequest(
            supply_id="70", row_version=2, timeslot_start="2026-06-11T10:00:00Z"
        )
        response = await api.fbp_order_direct_timeslot_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/timeslot/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDirectTimeslotEditResponse)
        assert response.error_reasons == ["LOGISTICS_REASON"]


class TestFbpOrderDirectTimeslotList:
    """Тесты для метода fbp_order_direct_timeslot_list."""

    @pytest.mark.asyncio
    async def test_fbp_order_direct_timeslot_list(self, api, mock_api_request):
        """Тестирует метод fbp_order_direct_timeslot_list."""
        mock_api_request.return_value = {
            "timeslots": [
                {"timeslot_start": "2026-06-10T10:00:00Z", "timeslot_end": "2026-06-10T12:00:00Z"}
            ],
            "warehouse_timezone_name": "Europe/Moscow",
            "reasons": [],
        }

        request = FbpOrderDirectTimeslotListRequest(
            supply_id="70",
            interval_start="2026-06-10T00:00:00Z",
            interval_end="2026-06-12T00:00:00Z",
        )
        response = await api.fbp_order_direct_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/timeslot/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDirectTimeslotListResponse)
        assert len(response.timeslots) == 1
        assert response.warehouse_timezone_name == "Europe/Moscow"


class TestFbpOrderDropOffCancel:
    """Тесты для метода fbp_order_drop_off_cancel."""

    @pytest.mark.asyncio
    async def test_fbp_order_drop_off_cancel(self, api, mock_api_request):
        """Тестирует метод fbp_order_drop_off_cancel."""
        mock_api_request.return_value = {"is_error": False, "row_version": 2}

        request = FbpOrderDropOffCancelRequest(supply_id="70")
        response = await api.fbp_order_drop_off_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/cancel",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDropOffCancelResponse)
        assert response.is_error is False


class TestFbpOrderDropOffDlvEdit:
    """Тесты для метода fbp_order_drop_off_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_order_drop_off_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_order_drop_off_dlv_edit."""
        mock_api_request.return_value = {"row_version": 3}

        request = FbpOrderDropOffDlvEditRequest(
            supply_id="70", row_version=2, drop_off_date="2026-06-11T10:00:00Z"
        )
        response = await api.fbp_order_drop_off_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDropOffDlvEditResponse)
        assert response.row_version == 3


class TestFbpOrderDropOffTimetable:
    """Тесты для метода fbp_order_drop_off_timetable."""

    @pytest.mark.asyncio
    async def test_fbp_order_drop_off_timetable(self, api, mock_api_request):
        """Тестирует метод fbp_order_drop_off_timetable."""
        mock_api_request.return_value = {
            "calendar": [
                {
                    "day_of_week": "TUESDAY",
                    "calendar_item": {
                        "opening_hours": {"timeslot_start": "08:00", "timeslot_end": "20:00"},
                        "is_holiday": False,
                    },
                }
            ]
        }

        request = FbpOrderDropOffTimetableRequest(
            warehouse_id=123, province_uuid="uuid-1", drop_off_point_id=7
        )
        response = await api.fbp_order_drop_off_timetable(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/timetable",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderDropOffTimetableResponse)
        assert response.calendar[0].day_of_week == "TUESDAY"


class TestFbpOrderPickUpCancel:
    """Тесты для метода fbp_order_pick_up_cancel."""

    @pytest.mark.asyncio
    async def test_fbp_order_pick_up_cancel(self, api, mock_api_request):
        """Тестирует метод fbp_order_pick_up_cancel."""
        mock_api_request.return_value = {"is_error": False, "row_version": 2}

        request = FbpOrderPickUpCancelRequest(supply_id="70")
        response = await api.fbp_order_pick_up_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/pick-up/cancel",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderPickUpCancelResponse)
        assert response.is_error is False


class TestFbpOrderPickUpDlvEdit:
    """Тесты для метода fbp_order_pick_up_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_order_pick_up_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_order_pick_up_dlv_edit."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {"order_errors": ["PICK_UP_SENDER_NAME_IS_EMPTY"]},
            "row_version": 2,
        }

        request = FbpOrderPickUpDlvEditRequest(
            supply_id="70",
            row_version=1,
            pickup_details=FbpOrderPickUpEditDetails(
                sender_name="Иванов И.И.", sender_phone="+79990000000"
            ),
        )
        response = await api.fbp_order_pick_up_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/pick-up/dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderPickUpDlvEditResponse)
        assert response.error.order_errors == ["PICK_UP_SENDER_NAME_IS_EMPTY"]
