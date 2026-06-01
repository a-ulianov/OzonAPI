import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSAggregatorDeliveryMethodUpdateRequest,
    WarehouseERFBSOperationResponse,
)


class TestWarehouseERFBSAggregatorDeliveryMethodUpdate:
    """Тесты для метода warehouse_erfbs_aggregator_delivery_method_update."""

    @pytest.mark.asyncio
    async def test_warehouse_erfbs_aggregator_delivery_method_update(self, api, mock_api_request):
        """Тестирует метод warehouse_erfbs_aggregator_delivery_method_update."""

        mock_api_request.return_value = {"operation_id": "op-erfbs-agg-dm-1"}

        request = WarehouseERFBSAggregatorDeliveryMethodUpdateRequest(
            warehouse_id=123,
            delivery_method_id=456,
            name="Партнёры Ozon",
            cut_in=120,
            deliver_to_pvz=False,
            return_settings={"return_method": "TRANSPORT_COMPANY", "transport_company_name": "СДЭК"},
        )

        response = await api.warehouse_erfbs_aggregator_delivery_method_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/aggregator/delivery-method/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-erfbs-agg-dm-1"
