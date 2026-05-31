import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerPlaceIntoRequest,
    CarriageContainerPlaceIntoResponse,
)


class TestCarriageContainerPlaceInto:
    """Тесты для метода carriage_container_place_into."""

    @pytest.mark.asyncio
    async def test_carriage_container_place_into(self, api, mock_api_request):
        """Тестирует метод carriage_container_place_into."""

        mock_response_data = {"task_id": 779, "error_containers": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerPlaceIntoRequest(
            parent_container_id=12345, child_container_ids=["67890"]
        )

        response = await api.carriage_container_place_into(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/place-into",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerPlaceIntoResponse)
        assert response.task_id == 779
