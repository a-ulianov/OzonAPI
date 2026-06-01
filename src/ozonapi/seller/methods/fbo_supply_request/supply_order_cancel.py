from ...core import APIManager
from ...schemas.fbo_supply_request import (
    SupplyOrderCancelRequest,
    SupplyOrderCancelResponse,
)


class SupplyOrderCancelMixin(APIManager):
    """Реализует метод /v1/supply-order/cancel"""

    async def supply_order_cancel(
            self: "SupplyOrderCancelMixin",
            request: SupplyOrderCancelRequest
    ) -> SupplyOrderCancelResponse:
        """Запускает отмену заявки на поставку FBO.

        Notes:
            • Асинхронная операция; статус — через `supply_order_cancel_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderCancel

        Args:
            request: Запрос отмены заявки по схеме `SupplyOrderCancelRequest`

        Returns:
            Идентификатор операции по схеме `SupplyOrderCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_cancel(
                    SupplyOrderCancelRequest(order_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/cancel",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderCancelResponse(**response)
