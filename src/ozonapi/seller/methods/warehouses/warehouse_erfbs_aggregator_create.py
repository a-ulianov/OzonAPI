from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSAggregatorCreateRequest,
    WarehouseERFBSOperationResponse,
)


class WarehouseERFBSAggregatorCreateMixin(APIManager):
    """Реализует метод /v1/warehouse/erfbs/aggregator/create"""

    async def warehouse_erfbs_aggregator_create(
            self: "WarehouseERFBSAggregatorCreateMixin",
            request: WarehouseERFBSAggregatorCreateRequest
    ) -> WarehouseERFBSOperationResponse:
        """Создаёт склад rFBS Express с методом доставки «Партнёры Ozon».

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSAggregatorCreate

        Args:
            request: Запрос по схеме `WarehouseERFBSAggregatorCreateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_erfbs_aggregator_create(
                    WarehouseERFBSAggregatorCreateRequest(name="Склад", phone="+70000000000")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/aggregator/create",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseERFBSOperationResponse(**response)
