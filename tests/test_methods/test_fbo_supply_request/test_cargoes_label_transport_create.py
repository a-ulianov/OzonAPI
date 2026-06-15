import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesLabelTransportCreateRequest,
    CargoesLabelTransportCreateResponse,
)


class TestCargoesLabelTransportCreate:
    """Тесты для метода cargoes_label_transport_create."""

    @pytest.mark.asyncio
    async def test_cargoes_label_transport_create(self, api, mock_api_request):
        """Тестирует метод cargoes_label_transport_create."""

        mock_api_request.return_value = {
            "operation_id": "op-lt-1",
            "error_reasons": [],
        }

        request = CargoesLabelTransportCreateRequest(
            supply_id=123, transport_cargo_ids=["10"]
        )

        response = await api.cargoes_label_transport_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesLabelTransportCreateResponse)
        assert response.operation_id == "op-lt-1"
