from ..core import APIManager

from ..schemas.prices_and_stocks import (
    ProductInfoPricesRequest,
    ProductInfoPricesResponse,
    ProductInfoStocksRequest,
    ProductInfoStocksResponse,
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
)


class SellerPricesAndStocksAPI(APIManager):
    """Реализует методы раздела Цены и остатки товаров.

    References:
        https://docs.ozon.ru/api/seller/#tag/PricesandStocksAPI
    """

    async def product_info_prices(
        self: "SellerPricesAndStocksAPI",
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
            json=request.model_dump(),
        )
        return ProductInfoPricesResponse(**response)

    async def product_info_stocks(
        self: "SellerPricesAndStocksAPI",
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
            json=request.model_dump(),
        )
        return ProductInfoStocksResponse(**response)

    async def product_info_stocks_by_warehouse_fbs(
        self: "SellerPricesAndStocksAPI",
        request: ProductInfoStocksByWarehouseFBSRequest
    ) -> ProductInfoStocksByWarehouseFBSResponse:
        """Метод для получения информации о складских остатках и зарезервированном кол-ве в разбивке по складам продавца (FBS и rFBS) по SKU.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbs

        Args:
            request: Список SKU для получения информации о товарах о складских остатках и зарезервированном кол-ве в разбивке по складам продавца (FBS и rFBS) по схеме `ProductInfoStocksByWarehouseFBSRequest`

        Returns:
            Ответ с информацией о складских остатках и зарезервированном кол-ве в разбивке по складам продавца (FBS и rFBS) по схеме `ProductInfoStocksByWarehouseFBSResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_stocks_by_warehouse_fbs(
                    ProductInfoStocksByWarehouseFBSRequest(
                        sku=[9876543210, ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            json=request.model_dump(),
        )
        return ProductInfoStocksByWarehouseFBSResponse(**response)