import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportActivateStatusRequest,
    CargoesTransportActivateStatusResponse,
)


class TestCargoesTransportActivateStatus:
    """Тесты для метода cargoes_transport_activate_status."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_activate_status(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_activate_status."""

        mock_api_request.return_value = {
            "status": "IN_PROGRESS",
            "error_reasons": [],
        }

        request = CargoesTransportActivateStatusRequest(operation_id="op-ta-1")

        response = await api.cargoes_transport_activate_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/activate/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportActivateStatusResponse)
        assert response.status == "IN_PROGRESS"
