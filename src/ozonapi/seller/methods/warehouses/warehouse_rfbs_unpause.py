from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseRfbsUnpauseRequest,
)


class WarehouseRfbsUnpauseMixin(APIManager):
    """Реализует метод /v1/warehouse/rfbs/unpause"""

    async def warehouse_rfbs_unpause(
            self: "WarehouseRfbsUnpauseMixin",
            request: WarehouseRfbsUnpauseRequest
    ) -> WarehouseERFBSOperationResponse:
        """Снимает rFBS-склад с паузы.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseRfbsUnpause

        Args:
            request: Запрос по схеме `WarehouseRfbsUnpauseRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_rfbs_unpause(
                    WarehouseRfbsUnpauseRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/rfbs/unpause",
            payload=request.model_dump()
        )
        return WarehouseERFBSOperationResponse(**response)
