from ...core import APIManager
from ...schemas.prices_and_stocks import ProductImportPricesRequest, ProductImportPricesResponse


class ProductImportPricesMixin(APIManager):
    """Реализует метод /v1/product/import/prices"""

    async def product_import_prices(
            self: "ProductImportPricesMixin",
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
                                manage_elastic_boosting_through_price=True,
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
            payload=request.model_dump(),
        )
        return ProductImportPricesResponse(**response)
