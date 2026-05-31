import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerGetRequest,
    CarriageContainerGetResponse,
)


class TestCarriageContainerGet:
    """Тесты для метода carriage_container_get."""

    @pytest.mark.asyncio
    async def test_carriage_container_get(self, api, mock_api_request):
        """Тестирует метод carriage_container_get."""

        mock_response_data = {
            "container_id": 12345,
            "cargo_type": "box",
            "status": "new",
            "count_of_postings": 1,
            "weight": 1.2,
            "warehouse_id": 999,
            "related_container_ids": ["67890"],
            "postings": [
                {
                    "posting_number": "33920113-1231-1",
                    "weight": 1.2,
                    "products": [
                        {"sku": 987654, "name": "Товар", "offer_id": "ART-1", "quantity": 1}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerGetRequest(container_id=12345)

        response = await api.carriage_container_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/get",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerGetResponse)
        assert response.container_id == 12345
        assert response.postings[0].products[0].sku == 987654
