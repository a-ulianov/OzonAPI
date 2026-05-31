import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerRemoveFromRequest,
    CarriageContainerRemoveFromResponse,
)


class TestCarriageContainerRemoveFrom:
    """Тесты для метода carriage_container_remove_from."""

    @pytest.mark.asyncio
    async def test_carriage_container_remove_from(self, api, mock_api_request):
        """Тестирует метод carriage_container_remove_from."""

        mock_response_data = {"task_id": 781, "error_containers": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerRemoveFromRequest(
            parent_container_id=12345, child_container_ids=["67890"]
        )

        response = await api.carriage_container_remove_from(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/remove-from",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerRemoveFromResponse)
        assert response.task_id == 781
