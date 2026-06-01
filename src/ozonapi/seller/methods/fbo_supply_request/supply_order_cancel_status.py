from ...core import APIManager
from ...schemas.fbo_supply_request import (
    SupplyOrderCancelStatusRequest,
    SupplyOrderCancelStatusResponse,
)


class SupplyOrderCancelStatusMixin(APIManager):
    """Реализует метод /v1/supply-order/cancel/status"""

    async def supply_order_cancel_status(
            self: "SupplyOrderCancelStatusMixin",
            request: SupplyOrderCancelStatusRequest
    ) -> SupplyOrderCancelStatusResponse:
        """Возвращает статус отмены заявки на поставку FBO.

        Notes:
            • Используйте `operation_id`, полученный методом `supply_order_cancel()`.
            • В `result.supplies` возвращается результат отмены по каждой поставке.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderCancelStatus

        Args:
            request: Запрос статуса отмены по схеме `SupplyOrderCancelStatusRequest`

        Returns:
            Статус отмены заявки по схеме `SupplyOrderCancelStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_cancel_status(
                    SupplyOrderCancelStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/cancel/status",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderCancelStatusResponse(**response)
