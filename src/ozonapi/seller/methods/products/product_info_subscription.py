from ...core import APIManager
from ...schemas.products import ProductInfoSubscriptionRequest, ProductInfoSubscriptionResponse


class ProductInfoSubscriptionMixin(APIManager):
    """Реализует метод /v1/product/info/subscription"""

    async def product_info_subscription(
        self: "ProductInfoSubscriptionMixin",
        request: ProductInfoSubscriptionRequest
    ) -> ProductInfoSubscriptionResponse:
        """Получает по SKU количество пользователей, подписавшихся на уведомление о поступлении товара.

        Notes:
            • Метод возвращает количество пользователей, которые нажали «Узнать о поступлении» на странице товара.
            • Вы можете передать несколько товаров в одном запросе.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductInfoSubscription

        Args:
            request: Список SKU товаров для получения информации о подписках по схеме `ProductInfoSubscriptionRequest`.

        Returns:
            Количество подписавшихся пользователей для каждого товара по схеме `ProductInfoSubscriptionResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_subscription(
                    ProductInfoSubscriptionRequest(
                        skus=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/subscription",
            payload=request.model_dump(),
        )
        return ProductInfoSubscriptionResponse(**response)
