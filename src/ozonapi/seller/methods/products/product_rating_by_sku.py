from ...core import APIManager
from ...schemas.products import ProductRatingBySkuRequest, ProductRatingBySkuResponse


class ProductRatingBySkuMixin(APIManager):
    """Реализует метод /v1/product/rating-by-sku"""

    async def product_rating_by_sku(
        self: "ProductRatingBySkuMixin",
        request: ProductRatingBySkuRequest
    ) -> ProductRatingBySkuResponse:
        """Получает по SKU контент-рейтинг товаров и рекомендации по его увеличению.

        Notes:
            • Контент-рейтинг товара рассчитывается от `0` до `100`.
            • Метод возвращает детальную информацию по группам характеристик, влияющим на рейтинг.
            • В ответе содержатся рекомендации по заполнению атрибутов для улучшения рейтинга.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductRatingBySku

        Args:
            request: Список SKU товаров для получения контент-рейтинга по схеме `ProductRatingBySkuRequest`.

        Returns:
            Контент-рейтинг товаров с детализацией по группам характеристик по схеме `ProductRatingBySkuResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_rating_by_sku(
                    ProductRatingBySkuRequest(
                        skus=[179737222, 179737223]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/rating-by-sku",
            payload=request.model_dump(),
        )
        return ProductRatingBySkuResponse(**response)
