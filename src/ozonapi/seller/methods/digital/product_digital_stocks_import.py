from ...core import APIManager
from ...schemas.digital import (
    ProductDigitalStocksImportRequest,
    ProductDigitalStocksImportResponse,
)


class ProductDigitalStocksImportMixin(APIManager):
    """Реализует метод /v1/product/digital/stocks/import"""

    async def product_digital_stocks_import(
            self: "ProductDigitalStocksImportMixin",
            request: ProductDigitalStocksImportRequest
    ) -> ProductDigitalStocksImportResponse:
        """Обновляет количество цифровых товаров на складе.

        Notes:
            • За один запрос можно обновить остатки по нескольким товарам.
            • По каждому товару в ответе возвращается признак `updated` и список
              ошибок `errors`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DigitalProductAPI_StocksImport

        Args:
            request: Запрос на обновление остатков по схеме
                `ProductDigitalStocksImportRequest`

        Returns:
            Статусы обновления остатков по схеме `ProductDigitalStocksImportResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_digital_stocks_import(
                    ProductDigitalStocksImportRequest(
                        stocks=[{"offer_id": "DIGITAL-1", "stock": 100}]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/digital/stocks/import",
            payload=request.model_dump()
        )
        return ProductDigitalStocksImportResponse(**response)
