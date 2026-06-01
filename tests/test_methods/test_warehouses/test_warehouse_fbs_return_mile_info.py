import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSReturnMileInfoRequest,
    WarehouseFBSReturnMileInfoResponse,
)


class TestWarehouseFBSReturnMileInfo:
    """Тесты для метода warehouse_fbs_return_mile_info."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_return_mile_info(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_return_mile_info."""

        mock_api_request.return_value = {
            "return_mile_settings": [
                {
                    "is_return_mile_required": True,
                    "return_point": {
                        "address": "Москва",
                        "id": 300,
                        "name": "Возврат-1",
                        "type": "PVZ",
                        "utc_offset": 180,
                    },
                    "warehouse_id": 123,
                }
            ]
        }

        request = WarehouseFBSReturnMileInfoRequest(warehouse_ids=["123"])

        response = await api.warehouse_fbs_return_mile_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/return-mile/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSReturnMileInfoResponse)
        assert response.return_mile_settings[0].warehouse_id == 123
        assert response.return_mile_settings[0].return_point.id == 300
