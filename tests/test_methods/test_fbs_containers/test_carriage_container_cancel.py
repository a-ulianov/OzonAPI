import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerCancelRequest,
    CarriageContainerCancelResponse,
)


class TestCarriageContainerCancel:
    """Тесты для метода carriage_container_cancel."""

    @pytest.mark.asyncio
    async def test_carriage_container_cancel(self, api, mock_api_request):
        """Тестирует метод carriage_container_cancel."""

        mock_response_data = {"task_id": 782, "error_containers": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerCancelRequest(container_ids=["12345"])

        response = await api.carriage_container_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/cancel",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerCancelResponse)
        assert response.task_id == 782
