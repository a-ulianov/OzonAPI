from ...core import APIManager
from ...schemas.products import ProductImportBySkuRequest, ProductImportBySkuResponse


class ProductImportBySkuMixin(APIManager):
    """Реализует метод /v1/product/import-by-sku"""

    async def product_import_by_sku(
        self: "ProductImportBySkuMixin",
        request: ProductImportBySkuRequest
    ) -> ProductImportBySkuResponse:
        """Создаёт копию карточки товара с указанным SKU.

        Notes:
            • Создать копию не получится, если продавец запретил копирование своих карточек.
            • Обновить товар по SKU нельзя.
            • Запросы обрабатываются очередями.
            • Для получения детализированной информации о результате выполнения операции используйте метод `product_import_info()`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ImportProductsBySKU

        Args:
            request: SKU с которого делается копия и ряд свойств для нового товара по схеме `ProductImportBySkuRequest`

        Returns:
            Айдишник таски для `product_import_info()` и список `product_id` по схеме `ProductImportBySkuResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_import_by_sku(
                    ProductImportBySkuRequest(
                        items=[
                            ProductImportBySkuRequestItem(
                                sku=298789742,
                                name="Новый товар",
                                offer_id="article-12345",
                                currency_code=CurrencyCode.RUB,
                                old_price="2590.00",
                                price="2300.00",
                                vat=VAT.TEN_PERCENT
                            ),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import-by-sku",
            payload=request.model_dump(),
        )
        return ProductImportBySkuResponse(**response)
