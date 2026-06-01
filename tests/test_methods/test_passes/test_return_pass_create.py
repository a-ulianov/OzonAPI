import pytest

from src.ozonapi.seller.schemas.passes import (
    ReturnPassCreateRequest,
    ReturnPassCreateResponse,
)


class TestReturnPassCreate:
    """Тесты для метода return_pass_create."""

    @pytest.mark.asyncio
    async def test_return_pass_create(self, api, mock_api_request):
        """Тестирует метод return_pass_create."""

        mock_api_request.return_value = {"arrival_pass_ids": [456]}

        request = ReturnPassCreateRequest(
            arrival_passes=[
                {
                    "arrival_time": "2026-06-02T08:00:00Z",
                    "dropoff_point_id": 10,
                    "warehouse_id": 20,
                    "driver_name": "Иванов И.И.",
                    "driver_phone": "+79990000000",
                    "vehicle_license_plate": "А123БВ77",
                    "vehicle_model": "ГАЗель",
                }
            ],
        )

        response = await api.return_pass_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/pass/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnPassCreateResponse)
        assert response.arrival_pass_ids == [456]
