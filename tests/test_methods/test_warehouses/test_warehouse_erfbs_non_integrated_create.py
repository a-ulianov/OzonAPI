import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSNonIntegratedCreateRequest,
    WarehouseERFBSOperationResponse,
)


class TestWarehouseERFBSNonIntegratedCreate:
    """Тесты для метода warehouse_erfbs_non_integrated_create."""

    @pytest.mark.asyncio
    async def test_warehouse_erfbs_non_integrated_create(self, api, mock_api_request):
        """Тестирует метод warehouse_erfbs_non_integrated_create."""

        mock_api_request.return_value = {"operation_id": "op-erfbs-ni-1"}

        request = WarehouseERFBSNonIntegratedCreateRequest(
            address_coordinates={"latitude": 55.7, "longitude": 37.6},
            name="Склад НИ",
            phone="+70000000000",
            delivery_method={
                "name": "Своя доставка",
                "cut_in": 60,
                "courier_cutoff": 30,
                "delivery_polygons": [{"id": 1, "time": 90}],
                "return_settings": {"return_method": "COURIER"},
            },
        )

        response = await api.warehouse_erfbs_non_integrated_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/non-integrated/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-erfbs-ni-1"
