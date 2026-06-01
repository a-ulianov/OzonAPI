from ...core import APIManager
from ...schemas.orders import (
    OrderCancelStatusRequest,
    OrderCancelStatusResponse,
)


class OrderCancelStatusMixin(APIManager):
    """Реализует метод /v1/order/cancel/status"""

    async def order_cancel_status(
            self: "OrderCancelStatusMixin",
            request: OrderCancelStatusRequest
    ) -> OrderCancelStatusResponse:
        """Возвращает статус отмены заказа rFBS.

        Notes:
            • Возвращает текущий `state` отмены и номера отправлений заказа.

        References:
            https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancelStatus

        Args:
            request: Запрос статуса по схеме `OrderCancelStatusRequest`

        Returns:
            Статус отмены по схеме `OrderCancelStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.order_cancel_status(
                    OrderCancelStatusRequest(order_number="123-456")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="order/cancel/status",
            payload=request.model_dump(by_alias=True)
        )
        return OrderCancelStatusResponse(**response)
