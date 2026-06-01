from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest,
    WarehouseERFBSOperationResponse,
)


class WarehouseERFBSNonIntegratedDeliveryMethodUpdateMixin(APIManager):
    """Реализует метод /v1/warehouse/erfbs/non-integrated/delivery-method/update"""

    async def warehouse_erfbs_non_integrated_delivery_method_update(
            self: "WarehouseERFBSNonIntegratedDeliveryMethodUpdateMixin",
            request: WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest
    ) -> WarehouseERFBSOperationResponse:
        """Обновляет метод доставки «Вы или сторонняя служба» склада rFBS Express.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSNonIntegratedDeliveryMethodUpdate

        Args:
            request: Запрос по схеме `WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_erfbs_non_integrated_delivery_method_update(
                    WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest(
                        warehouse_id=123, delivery_method_id=456
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/non-integrated/delivery-method/update",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseERFBSOperationResponse(**response)
