from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseERFBSUpdateRequest,
)


class WarehouseERFBSUpdateMixin(APIManager):
    """Реализует метод /v1/warehouse/erfbs/update"""

    async def warehouse_erfbs_update(
            self: "WarehouseERFBSUpdateMixin",
            request: WarehouseERFBSUpdateRequest
    ) -> WarehouseERFBSOperationResponse:
        """Обновляет данные склада rFBS Express.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.
            • Настройки метода доставки обновляются отдельными методами
              `warehouse_erfbs_aggregator_delivery_method_update()` или
              `warehouse_erfbs_non_integrated_delivery_method_update()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSUpdate

        Args:
            request: Запрос по схеме `WarehouseERFBSUpdateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_erfbs_update(
                    WarehouseERFBSUpdateRequest(warehouse_id=123, name="Новое имя")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/update",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseERFBSOperationResponse(**response)
