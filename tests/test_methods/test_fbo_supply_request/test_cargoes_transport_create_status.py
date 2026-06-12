import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportCreateStatusRequest,
    CargoesTransportCreateStatusResponse,
)


class TestCargoesTransportCreateStatus:
    """Тесты для метода cargoes_transport_create_status."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_create_status(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_create_status."""

        mock_api_request.return_value = {
            "status": "SUCCESS",
            "error_reasons": [],
            "result": {
                "transport_cargoes": [{"id": 10, "type": "PALLET"}]
            },
        }

        request = CargoesTransportCreateStatusRequest(operation_id="op-tc-1")

        response = await api.cargoes_transport_create_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/create/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportCreateStatusResponse)
        assert response.status == "SUCCESS"
        assert response.result.transport_cargoes[0].id == 10
