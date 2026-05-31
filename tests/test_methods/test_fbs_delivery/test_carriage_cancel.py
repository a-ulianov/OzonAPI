import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageCancelRequest, CarriageCancelResponse


class TestCarriageCancel:
    """Тесты для метода carriage_cancel."""

    @pytest.mark.asyncio
    async def test_carriage_cancel(self, api, mock_api_request):
        """Тестирует метод carriage_cancel."""

        mock_response_data = {"carriage_status": "cancelled", "error": ""}
        mock_api_request.return_value = mock_response_data

        request = CarriageCancelRequest(carriage_id=12345)

        response = await api.carriage_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/cancel",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageCancelResponse)
        assert response.carriage_status == "cancelled"
