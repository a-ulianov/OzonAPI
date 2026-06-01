import pytest

from src.ozonapi.seller.schemas.passes import (
    PassListRequest,
    PassListResponse,
)


class TestPassList:
    """Тесты для метода pass_list."""

    @pytest.mark.asyncio
    async def test_pass_list(self, api, mock_api_request):
        """Тестирует метод pass_list."""

        mock_api_request.return_value = {
            "arrival_passes": [
                {
                    "arrival_pass_id": 456,
                    "arrival_reasons": ["FBS_DELIVERY"],
                    "arrival_time": "2026-06-02T08:00:00Z",
                    "driver_name": "Иванов И.И.",
                    "driver_phone": "+79990000000",
                    "dropoff_point_id": 10,
                    "is_active": True,
                    "vehicle_license_plate": "А123БВ77",
                    "vehicle_model": "ГАЗель",
                    "warehouse_id": 20,
                }
            ],
            "cursor": "next",
        }

        request = PassListRequest(
            limit=100, filter={"only_active_passes": True}
        )

        response = await api.pass_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="pass/list",
            payload=request.model_dump()
        )

        assert isinstance(response, PassListResponse)
        assert response.cursor == "next"
        assert response.arrival_passes[0].arrival_pass_id == 456
        assert response.arrival_passes[0].is_active is True
