import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    SupplyOrderContentUpdateItem,
    SupplyOrderContentUpdateRequest,
    SupplyOrderContentUpdateResponse,
)


class TestSupplyOrderContentUpdate:
    """Тесты для метода supply_order_content_update."""

    @pytest.mark.asyncio
    async def test_supply_order_content_update(self, api, mock_api_request):
        """Тестирует метод supply_order_content_update."""

        mock_api_request.return_value = {
            "errors": [],
            "operation_id": "op-upd-1",
        }

        request = SupplyOrderContentUpdateRequest(
            order_id=1,
            supply_id=2,
            items=[SupplyOrderContentUpdateItem(sku=10, quantity=3)],
        )

        response = await api.supply_order_content_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, SupplyOrderContentUpdateResponse)
        assert response.operation_id == "op-upd-1"
