import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportBindStatusRequest,
    CargoesTransportBindStatusResponse,
)


class TestCargoesTransportBindStatus:
    """Тесты для метода cargoes_transport_bind_status."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_bind_status(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_bind_status."""

        mock_api_request.return_value = {
            "status": "SUCCESS",
            "error_reasons": [],
        }

        request = CargoesTransportBindStatusRequest(operation_id="op-tb-1")

        response = await api.cargoes_transport_bind_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/bind/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportBindStatusResponse)
        assert response.status == "SUCCESS"
