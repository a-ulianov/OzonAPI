import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageCreateRequest, CarriageCreateResponse


class TestCarriageCreate:
    """Тесты для метода carriage_create."""

    @pytest.mark.asyncio
    async def test_carriage_create(self, api, mock_api_request):
        """Тестирует метод carriage_create."""

        mock_response_data = {"carriage_id": 12345}
        mock_api_request.return_value = mock_response_data

        request = CarriageCreateRequest(delivery_method_id=999, departure_date="2026-06-01")

        response = await api.carriage_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/create",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageCreateResponse)
        assert response.carriage_id == 12345
