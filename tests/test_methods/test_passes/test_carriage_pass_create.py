import pytest

from src.ozonapi.seller.schemas.passes import (
    CarriagePassCreateRequest,
    CarriagePassCreateResponse,
)


class TestCarriagePassCreate:
    """Тесты для метода carriage_pass_create."""

    @pytest.mark.asyncio
    async def test_carriage_pass_create(self, api, mock_api_request):
        """Тестирует метод carriage_pass_create."""

        mock_api_request.return_value = {"arrival_pass_ids": [456, 789]}

        request = CarriagePassCreateRequest(
            carriage_id=123,
            arrival_passes=[
                {
                    "driver_name": "Иванов И.И.",
                    "driver_phone": "+79990000000",
                    "vehicle_license_plate": "А123БВ77",
                    "vehicle_model": "ГАЗель",
                    "with_returns": True,
                }
            ],
        )

        response = await api.carriage_pass_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/pass/create",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriagePassCreateResponse)
        assert response.arrival_pass_ids == [456, 789]
