import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportActivateRequest,
    CargoesTransportActivateResponse,
)


class TestCargoesTransportActivate:
    """Тесты для метода cargoes_transport_activate."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_activate(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_activate."""

        mock_api_request.return_value = {"operation_id": "op-ta-1"}

        request = CargoesTransportActivateRequest(
            supply_id=123, is_transport=True
        )

        response = await api.cargoes_transport_activate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/activate",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportActivateResponse)
        assert response.operation_id == "op-ta-1"
