import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    SupplyOrderContentUpdateStatusRequest,
    SupplyOrderContentUpdateStatusResponse,
)


class TestSupplyOrderContentUpdateStatus:
    """Тесты для метода supply_order_content_update_status."""

    @pytest.mark.asyncio
    async def test_supply_order_content_update_status(self, api, mock_api_request):
        """Тестирует метод supply_order_content_update_status."""

        mock_api_request.return_value = {
            "errors": [],
            "new_bundle_id": "bundle-new-1",
            "status": "SUCCESS",
        }

        request = SupplyOrderContentUpdateStatusRequest(operation_id="op-upd-1")

        response = await api.supply_order_content_update_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, SupplyOrderContentUpdateStatusResponse)
        assert response.new_bundle_id == "bundle-new-1"
        assert response.status == "SUCCESS"
