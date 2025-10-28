from ...core import APIManager, method_rate_limit
from ...schemas.prices_and_stocks import ProductsStocksRequest, ProductsStocksResponse


class ProductsStocksMixin(APIManager):
    """Реализует метод /v2/products/stocks"""

    @method_rate_limit(limit_requests=80, interval_seconds=60)
    async def products_stocks(
            self: "ProductsStocksMixin",
            request: ProductsStocksRequest,
    ) -> ProductsStocksResponse:
        """Метод для обновления количества товаров на складах FBS и rFBS.

        Notes:
            • Переданный остаток — количество товара в наличии без учёта зарезервированных товаров (свободный остаток).
            • Перед обновлением остатков проверьте количество зарезервированных товаров с помощью метода `product_info_stocks_by_warehouse_fbs()`.
            • За один запрос можно изменить наличие для 100 пар товар-склад.
            • С одного аккаунта продавца можно отправить до 80 запросов в минуту.
            • Обновлять остатки у одной пары товар-склад можно только 1 раз в 30 секунд.
            • Вы можете задать наличие товара только после того, как его статус сменится на `price_sent`.
            • Остатки крупногабаритных товаров можно обновлять только на предназначенных для них складах.
            • Если запрос содержит оба параметра — `offer_id` и `product_id`, изменения применятся к товару с `offer_id`.
            • Для избежания неоднозначности используйте только один из параметров.

        References:
            https://docs.ozon.com/api/seller/#operation/ProductAPI_ProductsStocksV2

        Args:
            request: Массив данных для обновления остатков товаров на складах FBS и rFBS по схеме `ProductsStocksRequest`

        Returns:
            Массив с результатами обновления остатков на складах FBS и rFBS по схеме `ProductsStocksResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.products_stocks(
                    ProductsStocksRequest(
                        stocks=[
                            ProductsStocksItem(
                                offer_id="PH11042",
                                product_id=313455276,
                                stock=100,
                                warehouse_id=22142605386000
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="products/stocks",
            payload=request.model_dump(),
        )
        return ProductsStocksResponse(**response)