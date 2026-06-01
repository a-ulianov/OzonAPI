import pytest

from src.ozonapi.seller.schemas.passes import (
    CarriagePassDeleteRequest,
    CarriagePassDeleteResponse,
)


class TestCarriagePassDelete:
    """Тесты для метода carriage_pass_delete."""

    @pytest.mark.asyncio
    async def test_carriage_pass_delete(self, api, mock_api_request):
        """Тестирует метод carriage_pass_delete."""

        mock_api_request.return_value = {}

        request = CarriagePassDeleteRequest(
            carriage_id=123, arrival_pass_ids=[456, 789]
        )

        response = await api.carriage_pass_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/pass/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriagePassDeleteResponse)
