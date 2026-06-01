from ...core import APIManager
from ...schemas.orders import OrderCreateRequest, OrderCreateResponse


class OrderCreateMixin(APIManager):
    """Реализует метод /v2/order/create"""

    async def order_create(
            self: "OrderCreateMixin",
            request: OrderCreateRequest
    ) -> OrderCreateResponse:
        """Создаёт заказ rFBS.

        Notes:
            • Заказ можно разбить на несколько отправлений через `splits`.
            • `delivery_schema` задаёт схему доставки (MIX/FBO/FBS).

        References:
            https://docs.ozon.ru/api/seller/#operation/OrderAPI_OrderCreate

        Args:
            request: Запрос создания заказа по схеме `OrderCreateRequest`

        Returns:
            Номер заказа и отправлений по схеме `OrderCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.order_create(
                    OrderCreateRequest(delivery_schema=OrderDeliverySchema.FBS)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="order/create",
            payload=request.model_dump(by_alias=True)
        )
        return OrderCreateResponse(**response)
