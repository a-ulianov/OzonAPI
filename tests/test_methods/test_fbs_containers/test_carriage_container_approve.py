import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerApproveRequest,
    CarriageContainerApproveResponse,
)


class TestCarriageContainerApprove:
    """Тесты для метода carriage_container_approve."""

    @pytest.mark.asyncio
    async def test_carriage_container_approve(self, api, mock_api_request):
        """Тестирует метод carriage_container_approve."""

        mock_response_data = {"task_id": 778, "error_containers": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerApproveRequest(container_ids=["12345"])

        response = await api.carriage_container_approve(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/approve",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerApproveResponse)
        assert response.task_id == 778
