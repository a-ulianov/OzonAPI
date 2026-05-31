import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageDeliveryListV1Request, CarriageDeliveryListV1Response


class TestCarriageDeliveryListV1:
    """Тесты для метода carriage_delivery_list_v1 (v1)."""

    @pytest.mark.asyncio
    async def test_carriage_delivery_list_v1(self, api, mock_api_request):
        """Тестирует метод carriage_delivery_list_v1."""

        mock_response_data = {
            "result": [
                {
                    "delivery_method_id": 999,
                    "delivery_method_name": "Ozon Логистика",
                    "carriage_postings_count": 3,
                    "carriages": [
                        {"id": "12345", "postings_count": 3, "status": "received"}
                    ],
                    "errors": []
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageDeliveryListV1Request(delivery_method_id=999)

        response = await api.carriage_delivery_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/delivery/list",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageDeliveryListV1Response)
        assert response.result[0].delivery_method_id == 999
        assert response.result[0].carriages[0].id == "12345"
