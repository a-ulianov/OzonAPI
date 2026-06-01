from ...core import APIManager
from ...schemas.delivery import DeliveryCheckoutRequest, DeliveryCheckoutResponse


class DeliveryCheckoutMixin(APIManager):
    """Реализует метод /v2/delivery/checkout"""

    async def delivery_checkout(
            self: "DeliveryCheckoutMixin",
            request: DeliveryCheckoutRequest
    ) -> DeliveryCheckoutResponse:
        """Возвращает доступные варианты доставки для корзины покупателя.

        Notes:
            • Заказ может быть разбит на несколько частей (`splits`) с разными
              складами и методами доставки.
            • Недоступные варианты сопровождаются `unavailable_reason`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeliveryCheckout

        Args:
            request: Запрос по схеме `DeliveryCheckoutRequest`

        Returns:
            Варианты доставки по схеме `DeliveryCheckoutResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_checkout(
                    DeliveryCheckoutRequest(
                        delivery_schema="FBS",
                        items=[{"sku": 123, "quantity": 1}],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="delivery/checkout",
            payload=request.model_dump()
        )
        return DeliveryCheckoutResponse(**response)
