from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSAggregatorDeliveryMethodUpdateRequest,
    WarehouseERFBSOperationResponse,
)


class WarehouseERFBSAggregatorDeliveryMethodUpdateMixin(APIManager):
    """Реализует метод /v1/warehouse/erfbs/aggregator/delivery-method/update"""

    async def warehouse_erfbs_aggregator_delivery_method_update(
            self: "WarehouseERFBSAggregatorDeliveryMethodUpdateMixin",
            request: WarehouseERFBSAggregatorDeliveryMethodUpdateRequest
    ) -> WarehouseERFBSOperationResponse:
        """Обновляет метод доставки «Партнёры Ozon» склада rFBS Express.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSAggregatorDeliveryMethodUpdate

        Args:
            request: Запрос по схеме `WarehouseERFBSAggregatorDeliveryMethodUpdateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_erfbs_aggregator_delivery_method_update(
                    WarehouseERFBSAggregatorDeliveryMethodUpdateRequest(
                        warehouse_id=123, delivery_method_id=456
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/aggregator/delivery-method/update",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseERFBSOperationResponse(**response)
