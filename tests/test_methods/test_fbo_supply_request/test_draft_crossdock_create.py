import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import (
    SupplyDeliveryType,
    SupplyDropOffWarehouseType,
)
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftCrossdockCreateRequest,
    DraftTypedClusterInfo,
    DraftTypedCreateResponse,
    DraftTypedDeliveryInfo,
    DraftTypedDropOffWarehouse,
    DraftTypedItem,
)


class TestDraftCrossdockCreate:
    """Тесты для метода draft_crossdock_create."""

    @pytest.mark.asyncio
    async def test_draft_crossdock_create(self, api, mock_api_request):
        """Тестирует метод draft_crossdock_create."""

        mock_api_request.return_value = {"draft_id": 777, "errors": []}

        request = DraftCrossdockCreateRequest(
            cluster_info=DraftTypedClusterInfo(
                items=[DraftTypedItem(sku=123, quantity=10)],
                macrolocal_cluster_id=1,
            ),
            delivery_info=DraftTypedDeliveryInfo(
                drop_off_warehouse=DraftTypedDropOffWarehouse(
                    warehouse_id=100,
                    warehouse_type=SupplyDropOffWarehouseType.SORTING_CENTER,
                ),
                type=SupplyDeliveryType.DROPOFF,
            ),
        )

        response = await api.draft_crossdock_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/crossdock/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftTypedCreateResponse)
        assert response.draft_id == 777
