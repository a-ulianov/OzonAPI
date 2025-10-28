from ...core import APIManager
from ...schemas.prices_and_stocks import ProductInfoStocksRequest, ProductInfoStocksResponse


class ProductInfoStocksMixin(APIManager):
    """Реализует метод /v4/product/info/stocks"""

    async def product_info_stocks(
        self: "ProductInfoStocksMixin",
        request: ProductInfoStocksRequest = ProductInfoStocksRequest.model_construct()
    ) -> ProductInfoStocksResponse:
        """Метод для получения информации о количестве общих складских остатков и зарезервированном количестве для схем FBS и rFBS по товарным идентификаторам.
        Чтобы получить информацию об остатках по схеме FBO, используйте метод `analytics_stocks()`.

        Notes:
            • Можно использовать без параметров - выберет всё по максимальному лимиту.
            • Можно передавать до `1000` значений суммарно по `offer_id` и `product_id` или не передавать их вовсе, чтобы выбрать всё.
            • Максимум `1000` товаров на страницу, если не заданы `offer_id` и `product_id`.
            • Для пагинации передайте полученный `cursor` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocks

        Args:
            request: Данные для получения информации об общих остатках FBS и rFBS по схеме `ProductInfoStocksRequest`

        Returns:
            Ответ с информацией об общих остатках FBS и rFBS по схеме `ProductInfoStocksResponse`

        Examples:
            Базовый запрос:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_stocks()

            Запрос с настройками выборки (товары не в наличии):
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_stocks(
                        ProductInfoStocksRequest(
                            cursor="",
                            filter=ProductInfoStocksFilter(
                                offer_id=[],
                                product_id=[],
                                visibility = Visibility.EMPTY_STOCK,
                                with_quants=None
                            ),
                            limit=100
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="product/info/stocks",
            payload=request.model_dump(),
        )
        return ProductInfoStocksResponse(**response)
