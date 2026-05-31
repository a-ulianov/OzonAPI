import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerTaskInfoRequest,
    CarriageContainerTaskInfoResponse,
)


class TestCarriageContainerTaskInfo:
    """Тесты для метода carriage_container_task_info."""

    @pytest.mark.asyncio
    async def test_carriage_container_task_info(self, api, mock_api_request):
        """Тестирует метод carriage_container_task_info."""

        mock_response_data = {"status": "success", "error_message": ""}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerTaskInfoRequest(task_id=777)

        response = await api.carriage_container_task_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/task/info",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerTaskInfoResponse)
        assert response.status == "success"
