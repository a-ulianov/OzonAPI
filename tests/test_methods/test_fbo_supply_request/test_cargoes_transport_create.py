import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesTransportCreateItem,
    CargoesTransportCreateRequest,
    CargoesTransportCreateResponse,
)


class TestCargoesTransportCreate:
    """Тесты для метода cargoes_transport_create."""

    @pytest.mark.asyncio
    async def test_cargoes_transport_create(self, api, mock_api_request):
        """Тестирует метод cargoes_transport_create."""

        mock_api_request.return_value = {
            "operation_id": "op-tc-1",
            "error_reasons": [],
        }

        request = CargoesTransportCreateRequest(
            supply_id=123,
            transport_cargoes=[
                CargoesTransportCreateItem(count=1, type="PALLET")
            ],
        )

        response = await api.cargoes_transport_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesTransportCreateResponse)
        assert response.operation_id == "op-tc-1"
