import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseOperationStatusRequest,
    WarehouseOperationStatusResponse,
)


class TestWarehouseOperationStatus:
    """Тесты для метода warehouse_operation_status."""

    @pytest.mark.asyncio
    async def test_warehouse_operation_status(self, api, mock_api_request):
        """Тестирует метод warehouse_operation_status."""

        mock_api_request.return_value = {
            "error": {"code": "", "message": ""},
            "result": {"entity_id": 555},
            "status": "SUCCESS",
            "type": "ARCHIVE",
        }

        request = WarehouseOperationStatusRequest(operation_id="op-1")

        response = await api.warehouse_operation_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/operation/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseOperationStatusResponse)
        assert response.result.entity_id == 555
        assert response.status == "SUCCESS"
