import pytest

from src.ozonapi.seller.schemas.fbs_containers import (
    CarriageContainerRemovePostingsRequest,
    CarriageContainerRemovePostingsResponse,
)


class TestCarriageContainerRemovePostings:
    """Тесты для метода carriage_container_remove_postings."""

    @pytest.mark.asyncio
    async def test_carriage_container_remove_postings(self, api, mock_api_request):
        """Тестирует метод carriage_container_remove_postings."""

        mock_response_data = {"task_id": 780, "error_postings": []}
        mock_api_request.return_value = mock_response_data

        request = CarriageContainerRemovePostingsRequest(
            container_id=12345, posting_numbers=["33920113-1231-1"]
        )

        response = await api.carriage_container_remove_postings(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/container/remove-postings",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageContainerRemovePostingsResponse)
        assert response.task_id == 780
