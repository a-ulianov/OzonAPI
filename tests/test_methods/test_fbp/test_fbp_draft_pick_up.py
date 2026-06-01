import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpDraftPickUpCreateRequest,
    FbpDraftPickUpCreateResponse,
    FbpDraftPickUpDeleteRequest,
    FbpDraftPickUpDeleteResponse,
    FbpDraftPickUpDlvEditRequest,
    FbpDraftPickUpDlvEditResponse,
    FbpDraftPickUpProductValidateRequest,
    FbpDraftPickUpProductValidateResponse,
    FbpDraftPickUpRegistrateRequest,
    FbpDraftPickUpRegistrateResponse,
    FbpPickUpDeliveryDetails,
    FbpProductValidateSkuItem,
)


def _pickup_details():
    return FbpPickUpDeliveryDetails(
        address="Москва, ул. Тестовая, 1",
        comment="Звонить заранее",
        date="2026-06-10T10:00:00Z",
        sender_name="Иванов И.И.",
        sender_phone="+79990000000",
    )


class TestFbpDraftPickUpCreate:
    """Тесты для метода fbp_draft_pick_up_create."""

    @pytest.mark.asyncio
    async def test_fbp_draft_pick_up_create(self, api, mock_api_request):
        """Тестирует метод fbp_draft_pick_up_create."""
        mock_api_request.return_value = {"draft_id": 30, "supply_id": "70", "row_version": 1}

        request = FbpDraftPickUpCreateRequest(
            bundle_id="b1",
            delivery_details=_pickup_details(),
            package_units_count=1,
            warehouse_id=123,
        )
        response = await api.fbp_draft_pick_up_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftPickUpCreateResponse)
        assert response.draft_id == 30


class TestFbpDraftPickUpDelete:
    """Тесты для метода fbp_draft_pick_up_delete."""

    @pytest.mark.asyncio
    async def test_fbp_draft_pick_up_delete(self, api, mock_api_request):
        """Тестирует метод fbp_draft_pick_up_delete."""
        mock_api_request.return_value = {
            "cancellation_state": {"cancellation_status": "CANCELED"},
            "row_version": 2,
        }

        request = FbpDraftPickUpDeleteRequest(supply_id="70")
        response = await api.fbp_draft_pick_up_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/delete",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftPickUpDeleteResponse)
        assert response.cancellation_state.cancellation_status == "CANCELED"


class TestFbpDraftPickUpDlvEdit:
    """Тесты для метода fbp_draft_pick_up_dlv_edit."""

    @pytest.mark.asyncio
    async def test_fbp_draft_pick_up_dlv_edit(self, api, mock_api_request):
        """Тестирует метод fbp_draft_pick_up_dlv_edit."""
        mock_api_request.return_value = {"row_version": 3}

        request = FbpDraftPickUpDlvEditRequest(
            supply_id="70", row_version=2, pickup_details=_pickup_details()
        )
        response = await api.fbp_draft_pick_up_dlv_edit(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/dlv/edit",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftPickUpDlvEditResponse)
        assert response.row_version == 3


class TestFbpDraftPickUpRegistrate:
    """Тесты для метода fbp_draft_pick_up_registrate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_pick_up_registrate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_pick_up_registrate."""
        mock_api_request.return_value = {
            "is_error": True,
            "error": {
                "order_error": "INVALID_PICK_UP_DATE",
                "bundle_errors": [{"sku": 123, "errors": ["BANNED"]}],
            },
            "row_version": 2,
        }

        request = FbpDraftPickUpRegistrateRequest(supply_id="70", row_version=1)
        response = await api.fbp_draft_pick_up_registrate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/registrate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftPickUpRegistrateResponse)
        assert response.error.order_error == "INVALID_PICK_UP_DATE"
        assert response.error.bundle_errors[0].sku == 123


class TestFbpDraftPickUpProductValidate:
    """Тесты для метода fbp_draft_pick_up_product_validate."""

    @pytest.mark.asyncio
    async def test_fbp_draft_pick_up_product_validate(self, api, mock_api_request):
        """Тестирует метод fbp_draft_pick_up_product_validate."""
        mock_api_request.return_value = {
            "bundle_generated": True,
            "bundle_id": "bundle-3",
            "approved_items": [{"sku": 123, "name": "Товар", "quantity": 1}],
            "rejected_items": [],
        }

        request = FbpDraftPickUpProductValidateRequest(
            skus=[FbpProductValidateSkuItem(sku=123, count=1)],
            warehouse_id=123,
        )
        response = await api.fbp_draft_pick_up_product_validate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/product/validate",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftPickUpProductValidateResponse)
        assert response.bundle_id == "bundle-3"
        assert response.approved_items[0].sku == 123
