import pytest

from src.ozonapi.seller.schemas.passes import (
    CarriagePassUpdateRequest,
    CarriagePassUpdateResponse,
)


class TestCarriagePassUpdate:
    """Тесты для метода carriage_pass_update."""

    @pytest.mark.asyncio
    async def test_carriage_pass_update(self, api, mock_api_request):
        """Тестирует метод carriage_pass_update."""

        mock_api_request.return_value = {}

        request = CarriagePassUpdateRequest(
            carriage_id=123,
            arrival_passes=[
                {
                    "id": 456,
                    "driver_name": "Иванов И.И.",
                    "driver_phone": "+79990000000",
                    "vehicle_license_plate": "А123БВ77",
                    "vehicle_model": "ГАЗель",
                }
            ],
        )

        response = await api.carriage_pass_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/pass/update",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriagePassUpdateResponse)
