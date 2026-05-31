import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerFillRequest,
    CarriageContainerFillResponse,
)


class TestCarriageContainerFill:
    """Тесты для метода carriage_container_fill."""

    @pytest.mark.asyncio
    async def test_carriage_container_fill(self, api, mock_api_request):
        """Тестирует метод carriage_container_fill."""

        mock_response_data = {
            "task_id": 777,
            "error_postings": [{"posting_number": "33920113-1231-1", "error_message": "busy"}]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerFillRequest(
            container_id=12345, posting_numbers=["33920113-1231-1"]
        )

        response = await api.carriage_container_fill(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/fill",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerFillResponse)
        assert response.task_id == 777
        assert response.error_postings[0].posting_number == "33920113-1231-1"
