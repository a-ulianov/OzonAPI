import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseOzonListRequest,
    WarehouseOzonListResponse,
)


class TestWarehouseOzonList:
    """Тесты для метода warehouse_ozon_list."""

    @pytest.mark.asyncio
    async def test_warehouse_ozon_list(self, api, mock_api_request):
        """Тестирует метод warehouse_ozon_list."""

        mock_api_request.return_value = {
            "warehouses": [
                {
                    "warehouse_id": 123,
                    "name": "Склад Ozon Москва",
                    "short_name": "MSK",
                    "address": "Москва",
                    "timezone": "Europe/Moscow",
                    "is_active": True,
                    "warehouse_type": "FULL_FILLMENT",
                    "country_iso_numeric": 643,
                    "is_cross_dock": False,
                    "is_distribution_center": False,
                    "is_edo": True,
                    "is_express": False,
                    "is_for_supply": True,
                }
            ]
        }

        request = WarehouseOzonListRequest(warehouse_types=["FULL_FILLMENT"])

        response = await api.warehouse_ozon_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/ozon/list",
            payload=request.model_dump()
        )

        assert isinstance(response, WarehouseOzonListResponse)
        assert response.warehouses[0].warehouse_id == 123
        assert response.warehouses[0].warehouse_type == "FULL_FILLMENT"
        assert response.warehouses[0].is_for_supply is True
