from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseOperationStatusRequest,
    WarehouseOperationStatusResponse,
)


class WarehouseOperationStatusMixin(APIManager):
    """Реализует метод /v1/warehouse/operation/status"""

    async def warehouse_operation_status(
            self: "WarehouseOperationStatusMixin",
            request: WarehouseOperationStatusRequest
    ) -> WarehouseOperationStatusResponse:
        """Возвращает статус асинхронной операции со складом FBS.

        Notes:
            • Используйте `operation_id`, полученный методами архивации, создания
              или обновления склада.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetWarehouseFBSOperationStatus

        Args:
            request: Запрос статуса по схеме `WarehouseOperationStatusRequest`

        Returns:
            Статус операции по схеме `WarehouseOperationStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_operation_status(
                    WarehouseOperationStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/operation/status",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseOperationStatusResponse(**response)
