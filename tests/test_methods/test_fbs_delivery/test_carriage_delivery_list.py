import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageDeliveryListRequest, CarriageDeliveryListResponse


class TestCarriageDeliveryList:
    """Тесты для метода carriage_delivery_list (v2)."""

    @pytest.mark.asyncio
    async def test_carriage_delivery_list(self, api, mock_api_request):
        """Тестирует метод carriage_delivery_list."""

        mock_response_data = {
            "cursor": "next-cursor",
            "has_next": True,
            "methods": [
                {
                    "delivery_method_id": 999,
                    "delivery_method_name": "Ozon Логистика",
                    "carriage_postings_count": 5,
                    "carriages": [
                        {"id": 12345, "status": "received", "postings_count": 5}
                    ],
                    "errors": []
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageDeliveryListRequest(limit=100)

        response = await api.carriage_delivery_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="carriage/delivery/list",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageDeliveryListResponse)
        assert response.has_next is True
        assert response.methods[0].delivery_method_id == 999
        assert response.methods[0].carriages[0].id == 12345
