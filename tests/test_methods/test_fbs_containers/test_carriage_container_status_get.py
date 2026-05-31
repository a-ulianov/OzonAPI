import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerStatusGetRequest,
    CarriageContainerStatusGetResponse,
)


class TestCarriageContainerStatusGet:
    """Тесты для метода carriage_container_status_get."""

    @pytest.mark.asyncio
    async def test_carriage_container_status_get(self, api, mock_api_request):
        """Тестирует метод carriage_container_status_get."""

        mock_response_data = {
            "containers": [{"container_id": 12345, "status": "new"}]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerStatusGetRequest(container_ids=["12345"])

        response = await api.carriage_container_status_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/status/get",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerStatusGetResponse)
        assert response.containers[0].status == "new"
