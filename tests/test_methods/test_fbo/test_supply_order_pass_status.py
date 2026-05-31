import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderPassStatusRequest,
    SupplyOrderPassStatusResponse,
)


class TestSupplyOrderPassStatus:
    """Тесты для метода supply_order_pass_status."""

    @pytest.mark.asyncio
    async def test_supply_order_pass_status(self, api, mock_api_request):
        """Тестирует метод supply_order_pass_status."""

        mock_response_data = {"result": "Success", "errors": []}
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderPassStatusRequest(operation_id="operation-123")

        response = await api.supply_order_pass_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/pass/status",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderPassStatusResponse)
        assert response.result == "Success"
        assert response.errors == []
