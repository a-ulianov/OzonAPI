import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerListRequest,
    CarriageContainerListResponse,
)
from src.ozonapi.seller.schemas.fbs_containers.v1__carriage_container_list import (
    CarriageContainerListFilter,
)


class TestCarriageContainerList:
    """Тесты для метода carriage_container_list."""

    @pytest.mark.asyncio
    async def test_carriage_container_list(self, api, mock_api_request):
        """Тестирует метод carriage_container_list."""

        mock_response_data = {
            "cursor": "next",
            "containers": [
                {
                    "container_id": 12345,
                    "container_number": 1,
                    "cargo_type": "box",
                    "status": "new",
                    "count_of_postings": 3,
                    "weight": 2.5,
                    "warehouse_id": 999,
                    "available_actions": ["approve"]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerListRequest(
            filter=CarriageContainerListFilter(warehouse_id=999), limit=100
        )

        response = await api.carriage_container_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/list",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerListResponse)
        assert response.containers[0].container_id == 12345
        assert response.containers[0].weight == 2.5
