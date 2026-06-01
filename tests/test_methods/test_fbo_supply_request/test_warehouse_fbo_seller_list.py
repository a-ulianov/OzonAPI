import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import WarehouseFboSellerListResponse


class TestWarehouseFboSellerList:
    """Тесты для метода warehouse_fbo_seller_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbo_seller_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbo_seller_list."""

        mock_api_request.return_value = {
            "warehouses": [
                {
                    "seller_warehouse_id": 300,
                    "seller_warehouse_name": "Мой склад",
                    "is_active": True,
                    "is_pickup": False,
                    "courier_comment": "Звонить заранее",
                    "address": {
                        "address": "Москва",
                        "city": "Москва",
                        "country_code": "RU",
                        "coordinates": {"latitude": 55.7, "longitude": 37.6},
                    },
                    "contacts": {"phone_numbers": ["+70000000000"]},
                    "working_days": [
                        {
                            "day": "MONDAY",
                            "time_from_local": "09:00",
                            "time_to_local": "18:00",
                        }
                    ],
                }
            ]
        }

        response = await api.warehouse_fbo_seller_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbo/seller/list",
            payload={},
        )

        assert isinstance(response, WarehouseFboSellerListResponse)
        assert response.warehouses[0].seller_warehouse_id == 300
        assert response.warehouses[0].address.coordinates.longitude == 37.6
        assert response.warehouses[0].working_days[0].day == "MONDAY"
