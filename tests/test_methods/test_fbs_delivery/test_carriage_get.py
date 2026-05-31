import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageGetRequest, CarriageGetResponse


class TestCarriageGet:
    """Тесты для метода carriage_get."""

    @pytest.mark.asyncio
    async def test_carriage_get(self, api, mock_api_request):
        """Тестирует метод carriage_get."""

        mock_response_data = {
            "carriage_id": 12345,
            "status": "received",
            "delivery_method_id": 999,
            "containers_count": 2,
            "warehouse_id": 555,
            "cancel_availability": {
                "is_cancel_available": True,
                "reason": ""
            },
            "available_actions": ["get_shipping_list"],
            "arrival_pass_ids": [1374537]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageGetRequest(carriage_id=12345)

        response = await api.carriage_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/get",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageGetResponse)
        assert response.carriage_id == 12345
        assert response.status == "received"
        assert response.cancel_availability.is_cancel_available is True
        assert response.arrival_pass_ids == [1374537]
