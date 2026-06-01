from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseRfbsPauseRequest,
)


class WarehouseRfbsPauseMixin(APIManager):
    """Реализует метод /v1/warehouse/rfbs/pause"""

    async def warehouse_rfbs_pause(
            self: "WarehouseRfbsPauseMixin",
            request: WarehouseRfbsPauseRequest
    ) -> WarehouseERFBSOperationResponse:
        """Ставит rFBS-склад на паузу.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.
            • Снять склад с паузы можно методом `warehouse_rfbs_unpause()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseRfbsPause

        Args:
            request: Запрос по схеме `WarehouseRfbsPauseRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_rfbs_pause(
                    WarehouseRfbsPauseRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/rfbs/pause",
            payload=request.model_dump()
        )
        return WarehouseERFBSOperationResponse(**response)
