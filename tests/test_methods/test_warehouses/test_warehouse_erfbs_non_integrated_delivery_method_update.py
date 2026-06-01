import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest,
    WarehouseERFBSOperationResponse,
)


class TestWarehouseERFBSNonIntegratedDeliveryMethodUpdate:
    """Тесты для метода warehouse_erfbs_non_integrated_delivery_method_update."""

    @pytest.mark.asyncio
    async def test_warehouse_erfbs_non_integrated_delivery_method_update(self, api, mock_api_request):
        """Тестирует метод warehouse_erfbs_non_integrated_delivery_method_update."""

        mock_api_request.return_value = {"operation_id": "op-erfbs-ni-dm-1"}

        request = WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest(
            warehouse_id=123,
            delivery_method_id=456,
            name="Своя доставка",
            cut_in=60,
            courier_cutoff=15,
            return_settings={"return_method": "COURIER", "contact_days": 2},
        )

        response = await api.warehouse_erfbs_non_integrated_delivery_method_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/non-integrated/delivery-method/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-erfbs-ni-dm-1"
