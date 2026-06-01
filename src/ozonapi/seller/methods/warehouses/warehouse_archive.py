from ...core import APIManager
from ...schemas.warehouses import WarehouseArchiveRequest, WarehouseArchiveResponse


class WarehouseArchiveMixin(APIManager):
    """Реализует метод /v1/warehouse/archive"""

    async def warehouse_archive(
            self: "WarehouseArchiveMixin",
            request: WarehouseArchiveRequest
    ) -> WarehouseArchiveResponse:
        """Переносит склад FBS в архив.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ArchiveWarehouseFBS

        Args:
            request: Запрос архивации по схеме `WarehouseArchiveRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseArchiveResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_archive(
                    WarehouseArchiveRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/archive",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseArchiveResponse(**response)
