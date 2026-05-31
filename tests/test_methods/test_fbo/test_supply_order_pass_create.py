import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderPassCreateRequest,
    SupplyOrderPassCreateResponse,
    SupplyOrderVehicleInfo,
)


class TestSupplyOrderPassCreate:
    """Тесты для метода supply_order_pass_create."""

    @pytest.mark.asyncio
    async def test_supply_order_pass_create(self, api, mock_api_request):
        """Тестирует метод supply_order_pass_create."""

        mock_response_data = {"operation_id": "operation-123", "error_reasons": []}
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderPassCreateRequest(
            supply_order_id=1234567890,
            vehicle=SupplyOrderVehicleInfo(
                driver_name="Иванов Иван",
                driver_phone="+79991234567",
                vehicle_model="ГАЗель",
                vehicle_number="А123БВ777",
            ),
        )

        response = await api.supply_order_pass_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/pass/create",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderPassCreateResponse)
        assert response.operation_id == "operation-123"
        assert response.error_reasons == []
