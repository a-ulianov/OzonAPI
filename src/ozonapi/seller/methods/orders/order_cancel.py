from ...core import APIManager
from ...schemas.orders import OrderCancelRequest, OrderCancelResponse


class OrderCancelMixin(APIManager):
    """Реализует метод /v1/order/cancel"""

    async def order_cancel(
            self: "OrderCancelMixin",
            request: OrderCancelRequest
    ) -> OrderCancelResponse:
        """Отменяет заказ rFBS целиком.

        Notes:
            • Идентификаторы причин отмены доступны в справочнике причин отмены.
            • Перед отменой проверьте её доступность методом `order_cancel_check()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancel

        Args:
            request: Запрос отмены заказа по схеме `OrderCancelRequest`

        Returns:
            Результат отмены по схеме `OrderCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.order_cancel(
                    OrderCancelRequest(order_number="123-456", reason_id=352)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="order/cancel",
            payload=request.model_dump(by_alias=True)
        )
        return OrderCancelResponse(**response)
