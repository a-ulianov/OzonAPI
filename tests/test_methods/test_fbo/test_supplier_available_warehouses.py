import pytest

from src.ozonapi.seller.schemas.fbo import SupplierAvailableWarehousesResponse


class TestSupplierAvailableWarehouses:
    """Тесты для метода supplier_available_warehouses."""

    @pytest.mark.asyncio
    async def test_supplier_available_warehouses(self, api, mock_api_request):
        """Тестирует метод supplier_available_warehouses."""

        mock_response_data = {
            "result": [
                {"warehouse_id": 111, "name": "Хоругвино", "status": "AVAILABLE"}
            ]
        }
        mock_api_request.return_value = mock_response_data

        response = await api.supplier_available_warehouses()

        mock_api_request.assert_called_once_with(
            method="get",
            api_version="v1",
            endpoint="supplier/available_warehouses",
        )

        assert isinstance(response, SupplierAvailableWarehousesResponse)
        assert response.result == [
            {"warehouse_id": 111, "name": "Хоругвино", "status": "AVAILABLE"}
        ]
