import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportBindItem,
    CargoesTransportBindRequest,
    CargoesTransportBindResponse,
)


class TestCargoesTransportBind:
    """Тесты для метода cargoes_transport_bind."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_bind(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_bind."""

        mock_api_request.return_value = {
            "operation_id": "op-tb-1",
            "error_reasons": [],
        }

        request = CargoesTransportBindRequest(
            supply_id=123,
            transport_cargo_bind=[
                CargoesTransportBindItem(cargo_ids=["1"], transport_cargo_id=10)
            ],
        )

        response = await api.cargoes_transport_bind(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/bind",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportBindResponse)
        assert response.operation_id == "op-tb-1"
