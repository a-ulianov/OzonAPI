import pytest

from src.ozonapi.seller.schemas.passes import (
    ReturnPassUpdateRequest,
    ReturnPassUpdateResponse,
)


class TestReturnPassUpdate:
    """Тесты для метода return_pass_update."""

    @pytest.mark.asyncio
    async def test_return_pass_update(self, api, mock_api_request):
        """Тестирует метод return_pass_update."""

        mock_api_request.return_value = {}

        request = ReturnPassUpdateRequest(
            arrival_passes=[
                {
                    "arrival_pass_id": 456,
                    "arrival_time": "2026-06-02T08:00:00Z",
                    "driver_name": "Иванов И.И.",
                    "driver_phone": "+79990000000",
                    "vehicle_license_plate": "А123БВ77",
                    "vehicle_model": "ГАЗель",
                }
            ],
        )

        response = await api.return_pass_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/pass/update",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnPassUpdateResponse)
