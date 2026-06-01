from ...core import APIManager
from ...schemas.orders import (
    OrderCancelCheckRequest,
    OrderCancelCheckResponse,
)


class OrderCancelCheckMixin(APIManager):
    """Реализует метод /v1/order/cancel/check"""

    async def order_cancel_check(
            self: "OrderCancelCheckMixin",
            request: OrderCancelCheckRequest
    ) -> OrderCancelCheckResponse:
        """Проверяет возможность отмены заказа rFBS.

        Notes:
            • Возвращает флаг `cancellable` для заказа и по каждому отправлению,
              а для недоступных к отмене — причину в `why_not_cancellable`.

        References:
            https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCancelCheck

        Args:
            request: Запрос проверки по схеме `OrderCancelCheckRequest`

        Returns:
            Возможность отмены по схеме `OrderCancelCheckResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.order_cancel_check(
                    OrderCancelCheckRequest(order_number="123-456")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="order/cancel/check",
            payload=request.model_dump(by_alias=True)
        )
        return OrderCancelCheckResponse(**response)
