import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyCreateType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    WarehouseFboListRequest,
    WarehouseFboListResponse,
)


class TestWarehouseFboList:
    """Тесты для метода warehouse_fbo_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbo_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbo_list."""

        mock_api_request.return_value = {
            "search": [
                {
                    "address": "Москва, ул. Примерная",
                    "coordinates": {"latitude": 55.7, "longitude": 37.6},
                    "name": "Хоругвино",
                    "warehouse_id": 200,
                    "warehouse_type": "WAREHOUSE_TYPE_FULL_FILLMENT",
                }
            ]
        }

        request = WarehouseFboListRequest(
            filter_by_supply_type=[SupplyCreateType.DIRECT], search="Москва"
        )

        response = await api.warehouse_fbo_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbo/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFboListResponse)
        assert response.search[0].warehouse_id == 200
        assert response.search[0].coordinates.latitude == 55.7
