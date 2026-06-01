from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseUnarchiveRequest,
    WarehouseUnarchiveResponse,
)


class WarehouseUnarchiveMixin(APIManager):
    """Реализует метод /v1/warehouse/unarchive"""

    async def warehouse_unarchive(
            self: "WarehouseUnarchiveMixin",
            request: WarehouseUnarchiveRequest
    ) -> WarehouseUnarchiveResponse:
        """Переносит склад FBS из архива.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/UnarchiveWarehouseFBS

        Args:
            request: Запрос разархивации по схеме `WarehouseUnarchiveRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseUnarchiveResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_unarchive(
                    WarehouseUnarchiveRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/unarchive",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseUnarchiveResponse(**response)
