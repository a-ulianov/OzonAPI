import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesLabelTransportByOrderStatusRequest,
    CargoesLabelTransportByOrderStatusResponse,
)


class TestCargoesLabelTransportByOrderStatus:
    """Тесты для метода cargoes_label_transport_by_order_status."""

    @pytest.mark.asyncio
    async def test_cargoes_label_transport_by_order_status(
        self, api, mock_api_request
    ):
        """Тестирует метод cargoes_label_transport_by_order_status."""

        mock_api_request.return_value = {
            "status": "SUCCESS",
            "error_reasons": [],
            "result": {
                "file_url": "https://example.com/label.pdf",
                "skipped_supplies_ids": [],
            },
        }

        request = CargoesLabelTransportByOrderStatusRequest(operation_id="op-lto-1")

        response = await api.cargoes_label_transport_by_order_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport-by-order/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesLabelTransportByOrderStatusResponse)
        assert response.result.file_url == "https://example.com/label.pdf"
