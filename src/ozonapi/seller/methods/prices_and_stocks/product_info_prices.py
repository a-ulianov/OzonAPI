from ...core import APIManager
from ...schemas.prices_and_stocks import ProductInfoPricesRequest, ProductInfoPricesResponse


class ProductInfoPricesMixin(APIManager):
    """Реализует метод /v5/product/info/prices"""

    async def product_info_prices(
        self: "ProductInfoPricesMixin",
        request: ProductInfoPricesRequest = ProductInfoPricesRequest.model_construct(),
    ) -> ProductInfoPricesResponse:
        """Метод для получения информации о ценах и комиссиях товаров по их идентификаторам.

        Notes:
            • Можно вообще ничего не передавать - выберет всё по максимальному лимиту.
            • Можно передавать до `1000` значений суммарно по `offer_id` и `product_id` или не передавать их вовсе, чтобы выбрать всё.
            • Максимум `1000` товаров на страницу, если не заданы `offer_id` и `product_id`.
            • Для пагинации используйте `cursor` из ответа, передав его в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoPrices

        Args:
            request: Содержит товарные идентификаторы для получения информации о ценах и комиссиях по схеме `ProductInfoPricesRequest`

        Returns:
            Ответ с информацией о ценах и комиссиях по схеме `ProductInfoPricesResponse`

        Example:
            Базовый запрос:
                 async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_prices()

            Запрос с настройками выборки:
                 async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_prices(
                        ProductInfoPricesRequest(
                                cursor="",
                                filter=ProductInfoPricesFilter(
                                    offer_id=[],
                                    product_id=[],
                                    visibility = Visibility.VISIBLE,
                                ),
                                limit=100
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v5",
            endpoint="product/info/prices",
            payload=request.model_dump(),
        )
        return ProductInfoPricesResponse(**response)
