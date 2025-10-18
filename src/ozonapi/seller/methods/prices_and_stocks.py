from ..core import APIManager, method_rate_limit

from ..schemas.prices_and_stocks import (
    ProductInfoPricesRequest,
    ProductInfoPricesResponse,
    ProductInfoStocksRequest,
    ProductInfoStocksResponse,
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
    ProductImportPricesRequest,
    ProductImportPricesResponse, ProductsStocksRequest, ProductsStocksResponse,
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

    async def product_import_prices(
            self: "SellerPricesAndStocksAPI",
            request: ProductImportPricesRequest,
    ) -> ProductImportPricesResponse:
        """Метод для изменения цен одного или нескольких товаров.

        Notes:
            • Цену каждого товара можно обновлять не больше `10` раз в час.
            • Чтобы сбросить `old_price`, поставьте `0` у этого параметра.
            • Если у товара установлена минимальная цена и включено автоприменение в акции,
              отключите его и обновите минимальную цену, иначе вернётся ошибка `action_price_enabled_min_price_missing`.
            • Если запрос содержит оба параметра — `offer_id` и `product_id`, изменения применятся к товару с `offer_id`.
            • Для избежания неоднозначности используйте только один из параметров.
            • Максимум `1000` товаров в одном запросе.

        References:
            https://docs.ozon.com/api/seller/#operation/ProductAPI_ImportProductsPrices

        Args:
            request: Данные для изменения цен товаров по схеме `ProductImportPricesRequest`

        Returns:
            Ответ с результатами обновления цен по схеме `ProductImportPricesResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_import_prices(
                    ProductImportPricesRequest(
                        prices=[
                            ProductImportPricesItem(
                                auto_action_enabled=PricingStrategy.UNKNOWN,
                                auto_add_to_ozon_actions_list_enabled=PricingStrategy.UNKNOWN,
                                currency_code=CurrencyCode.RUB,
                                min_price="800",
                                min_price_for_auto_actions_enabled=True,
                                net_price="650",
                                offer_id="PH8865",
                                old_price="0",
                                price="1448",
                                price_strategy_enabled=PricingStrategy.UNKNOWN,
                                product_id=1386,
                                quant_size=1,
                                vat=VAT.PERCENT_20
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import/prices",
            json=request.model_dump(),
        )
        return ProductImportPricesResponse(**response)

    @method_rate_limit(limit_requests=80, interval_seconds=60)
    async def products_stocks(
            self: "SellerPricesAndStocksAPI",
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
            json=request.model_dump(),
        )
        return ProductsStocksResponse(**response)