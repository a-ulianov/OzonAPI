import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpDraftDirectCreateDeliveryDetails,
    FbpDraftDirectCreateRequest,
    FbpDraftDirectCreateResponse,
    FbpDraftDirectDeleteRequest,
    FbpDraftDirectDeleteResponse,
    FbpDraftDirectProductValidateRequest,
    FbpDraftDirectProductValidateResponse,
    FbpDraftDirectRegistrateRequest,
    FbpDraftDirectRegistrateResponse,
    FbpDraftDirectSellerDlvCreateDeliveryDetails,
    FbpDraftDirectSellerDlvCreateRequest,
    FbpDraftDirectSellerDlvCreateResponse,
    FbpDraftDirectSellerDlvEditRequest,
    FbpDraftDirectSellerDlvEditResponse,
    FbpDraftDirectTimeslotEditRequest,
    FbpDraftDirectTimeslotEditResponse,
    FbpDraftDirectTimeslotGetRequest,
    FbpDraftDirectTimeslotGetResponse,
    FbpDraftDirectTplDlvCreateDeliveryDetails,
    FbpDraftDirectTplDlvCreateRequest,
    FbpDraftDirectTplDlvCreateResponse,
    FbpDraftDirectTplDlvEditRequest,
    FbpDraftDirectTplDlvEditResponse,
    FbpProductValidateSkuItem,
)


class TestFbpDraftDirectCreate:
    """Тесты для метода fbp_draft_direct_create."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_create(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_create."""
        mock_api_request.return_value = {"draft_id": 10, "supply_id": "55", "row_version": 1}

        request = FbpDraftDirectCreateRequest(
            bundle_id="b1",
            delivery_details=FbpDraftDirectCreateDeliveryDetails(
                timeslot_start=["2026-06-10T10:00:00Z"]
            ),
            package_units_count=1,
            warehouse_id=123,
        )
        response = await api.fbp_draft_direct_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectCreateResponse)
        assert response.draft_id == 10
        assert response.supply_id == "55"


class TestFbpDraftDirectSellerDlvCreate:
    """Тесты для метода fbp_draft_direct_seller_dlv_create."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_seller_dlv_create(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_seller_dlv_create."""
        mock_api_request.return_value = {"draft_id": 11, "supply_id": "56", "row_version": 1}

        request = FbpDraftDirectSellerDlvCreateRequest(
            bundle_id="b1",
            delivery_details=FbpDraftDirectSellerDlvCreateDeliveryDetails(
                driver_name="Иванов",
                timeslot_start="2026-06-10T10:00:00Z",
                vehicle_number="А123ВС777",
                vehicle_type="Грузовой",
            ),
            package_units_count=1,
            warehouse_id=123,
        )
        response = await api.fbp_draft_direct_seller_dlv_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/seller-dlv/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectSellerDlvCreateResponse)
        assert response.draft_id == 11


class TestFbpDraftDirectTplDlvCreate:
    """Тесты для метода fbp_draft_direct_tpl_dlv_create."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_tpl_dlv_create(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_tpl_dlv_create."""
        mock_api_request.return_value = {"draft_id": 12, "supply_id": "57", "row_version": 1}

        request = FbpDraftDirectTplDlvCreateRequest(
            bundle_id="b1",
            delivery_details=FbpDraftDirectTplDlvCreateDeliveryDetails(
                timeslot_start="2026-06-10T10:00:00Z",
                tracking_number="TRK-1",
                transport_company_name="СДЭК",
            ),
            package_units_count=1,
            warehouse_id=123,
        )
        response = await api.fbp_draft_direct_tpl_dlv_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/tpl-dlv/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectTplDlvCreateResponse)
        assert response.draft_id == 12


class TestFbpDraftDirectSellerDlvEdit:
    """Тесты для метода fbp_draft_direct_seller_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_seller_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_seller_dlv_edit."""
        mock_api_request.return_value = {"is_error": False, "row_version": 2}

        request = FbpDraftDirectSellerDlvEditRequest(
            supply_id="55",
            row_version=1,
            driver_name="Иванов",
            vehicle_number="А123ВС777",
            vehicle_type="Грузовой",
        )
        response = await api.fbp_draft_direct_seller_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/seller-dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectSellerDlvEditResponse)
        assert response.is_error is False
        assert response.row_version == 2


class TestFbpDraftDirectTplDlvEdit:
    """Тесты для метода fbp_draft_direct_tpl_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_tpl_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_tpl_dlv_edit."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {"errors": ["DELIVERY_TRACKING_NUMBER_EMPTY"]},
            "row_version": 2,
        }

        request = FbpDraftDirectTplDlvEditRequest(
            supply_id="55",
            row_version=1,
            tracking_number="TRK-1",
            transport_company_name="СДЭК",
        )
        response = await api.fbp_draft_direct_tpl_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/tpl-dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectTplDlvEditResponse)
        assert response.is_error is True
        assert response.error.errors == ["DELIVERY_TRACKING_NUMBER_EMPTY"]


class TestFbpDraftDirectDelete:
    """Тесты для метода fbp_draft_direct_delete."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_delete(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_delete."""
        mock_api_request.return_value = {
            "cancellation_state": {"cancellation_status": "CANCELED"},
            "row_version": 3,
        }

        request = FbpDraftDirectDeleteRequest(supply_id="55")
        response = await api.fbp_draft_direct_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectDeleteResponse)
        assert response.cancellation_state.cancellation_status == "CANCELED"
        assert response.row_version == 3


class TestFbpDraftDirectRegistrate:
    """Тесты для метода fbp_draft_direct_registrate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_registrate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_registrate."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {
                "order_error": "INVALID_TIMESLOT",
                "bundle_errors": [{"sku": 123, "errors": ["NO_PRICE"]}],
            },
            "row_version": 2,
        }

        request = FbpDraftDirectRegistrateRequest(supply_id="55", row_version=1)
        response = await api.fbp_draft_direct_registrate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/registrate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectRegistrateResponse)
        assert response.is_error is True
        assert response.error.order_error == "INVALID_TIMESLOT"
        assert response.error.bundle_errors[0].sku == 123
        assert response.error.bundle_errors[0].errors == ["NO_PRICE"]


class TestFbpDraftDirectProductValidate:
    """Тесты для метода fbp_draft_direct_product_validate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_product_validate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_product_validate."""
        mock_api_request.return_value = {
            "bundle_generated": True,
            "bundle_id": "bundle-1",
            "approved_items": [{"sku": 123, "name": "Товар", "quantity": 2, "volume": 1.5}],
            "rejected_items": [
                {"sku": 456, "rejection_reasons": ["OUT_OF_ASSORTMENT"]}
            ],
        }

        request = FbpDraftDirectProductValidateRequest(
            skus=[FbpProductValidateSkuItem(sku=123, count=2)],
            warehouse_id=123,
        )
        response = await api.fbp_draft_direct_product_validate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/product/validate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectProductValidateResponse)
        assert response.bundle_generated is True
        assert response.bundle_id == "bundle-1"
        assert response.approved_items[0].sku == 123
        assert response.rejected_items[0].rejection_reasons == ["OUT_OF_ASSORTMENT"]


class TestFbpDraftDirectTimeslotGet:
    """Тесты для метода fbp_draft_direct_timeslot_get."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_timeslot_get(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_timeslot_get."""
        mock_api_request.return_value = {
            "timeslots": [
                {"timeslot_start": "2026-06-10T10:00:00Z", "timeslot_end": "2026-06-10T12:00:00Z"}
            ],
            "warehouse_timezone_name": "Europe/Moscow",
            "reasons": [],
        }

        request = FbpDraftDirectTimeslotGetRequest(
            bundle_id="b1",
            warehouse_id=123,
            interval_start="2026-06-10T00:00:00Z",
            interval_end="2026-06-12T00:00:00Z",
        )
        response = await api.fbp_draft_direct_timeslot_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/timeslot/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectTimeslotGetResponse)
        assert len(response.timeslots) == 1
        assert response.warehouse_timezone_name == "Europe/Moscow"


class TestFbpDraftDirectTimeslotEdit:
    """Тесты для метода fbp_draft_direct_timeslot_edit."""

    @pytest.mark.asyncio
    async def test_fbp_draft_direct_timeslot_edit(self, api, mock_api_request):
        """Тестирует метод fbp_draft_direct_timeslot_edit."""
        mock_api_request.return_value = {"error_reasons": ["NO_CAPACITY"], "row_version": 2}

        request = FbpDraftDirectTimeslotEditRequest(
            supply_id="55",
            row_version=1,
            timeslot_start="2026-06-11T10:00:00Z",
        )
        response = await api.fbp_draft_direct_timeslot_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/timeslot/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftDirectTimeslotEditResponse)
        assert response.error_reasons == ["NO_CAPACITY"]
        assert response.row_version == 2
