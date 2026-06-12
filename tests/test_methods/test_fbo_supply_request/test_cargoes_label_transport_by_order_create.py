import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesLabelTransportByOrderCreateRequest,
    CargoesLabelTransportByOrderCreateResponse,
)


class TestCargoesLabelTransportByOrderCreate:
    """Тесты для метода cargoes_label_transport_by_order_create."""

    @pytest.mark.asyncio
    async def test_cargoes_label_transport_by_order_create(
        self, api, mock_api_request
    ):
        """Тестирует метод cargoes_label_transport_by_order_create."""

        mock_api_request.return_value = {
            "operation_id": "op-lto-1",
            "error_reasons": [],
        }

        request = CargoesLabelTransportByOrderCreateRequest(order_id=123)

        response = await api.cargoes_label_transport_by_order_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport-by-order/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesLabelTransportByOrderCreateResponse)
        assert response.operation_id == "op-lto-1"
