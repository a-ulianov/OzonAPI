import pytest

from src.ozonapi.seller.schemas.delivery import (
    DeliveryCheckRequest,
    DeliveryCheckResponse,
)


class TestDeliveryCheck:
    """Тесты для метода delivery_check."""

    @pytest.mark.asyncio
    async def test_delivery_check(self, api, mock_api_request):
        """Тестирует метод delivery_check."""

        mock_api_request.return_value = {"is_possible": True}

        request = DeliveryCheckRequest(client_phone="+70000000000")

        response = await api.delivery_check(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery/check",
            payload=request.model_dump()
        )

        assert isinstance(response, DeliveryCheckResponse)
        assert response.is_possible is True
