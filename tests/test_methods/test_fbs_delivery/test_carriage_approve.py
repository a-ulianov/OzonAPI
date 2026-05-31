import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageApproveRequest, CarriageApproveResponse


class TestCarriageApprove:
    """Тесты для метода carriage_approve."""

    @pytest.mark.asyncio
    async def test_carriage_approve(self, api, mock_api_request):
        """Тестирует метод carriage_approve."""

        mock_response_data = {}
        mock_api_request.return_value = mock_response_data

        request = CarriageApproveRequest(carriage_id=12345, containers_count=3)

        response = await api.carriage_approve(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/approve",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageApproveResponse)
