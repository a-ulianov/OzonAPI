import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    SupplyOrderCancelStatusRequest,
    SupplyOrderCancelStatusResponse,
)


class TestSupplyOrderCancelStatus:
    """Тесты для метода supply_order_cancel_status."""

    @pytest.mark.asyncio
    async def test_supply_order_cancel_status(self, api, mock_api_request):
        """Тестирует метод supply_order_cancel_status."""

        mock_api_request.return_value = {
            "error_reasons": [],
            "result": {
                "is_order_cancelled": True,
                "supplies": [
                    {
                        "error_reasons": [],
                        "is_supply_cancelled": True,
                        "supply_id": 555,
                    }
                ],
            },
            "status": "SUCCESS",
        }

        request = SupplyOrderCancelStatusRequest(operation_id="op-cancel-1")

        response = await api.supply_order_cancel_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/cancel/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, SupplyOrderCancelStatusResponse)
        assert response.status == "SUCCESS"
        assert response.result.supplies[0].supply_id == 555
