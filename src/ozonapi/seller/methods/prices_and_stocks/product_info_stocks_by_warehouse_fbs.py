from ...core import APIManager
from ...schemas.prices_and_stocks import ProductInfoStocksByWarehouseFBSRequest, ProductInfoStocksByWarehouseFBSResponse


class ProductInfoStocksByWarehouseFBSMixin(APIManager):
    """Реализует метод /v2/product/info/stocks-by-warehouse/fbs"""

    async def product_info_stocks_by_warehouse_fbs(
        self: "ProductInfoStocksByWarehouseFBSMixin",
        request: ProductInfoStocksByWarehouseFBSRequest
    ) -> ProductInfoStocksByWarehouseFBSResponse:
        """Метод для получения информации о складских остатках и зарезервированном кол-ве в разбивке по складам продавца (FBS и rFBS).

        Notes:
            • Фильтровать можно по `sku` и/или `offer_id`.
            • Курсорная пагинация: если `has_next` равно true, передайте полученный `cursor`
              в следующий запрос, чтобы получить оставшиеся остатки.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbsV2

        Args:
            request: Параметры запроса по схеме `ProductInfoStocksByWarehouseFBSRequest` (limit, cursor, sku, offer_id)

        Returns:
            Ответ с информацией о складских остатках и зарезервированном кол-ве в разбивке по складам продавца (FBS и rFBS) по схеме `ProductInfoStocksByWarehouseFBSResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_stocks_by_warehouse_fbs(
                    ProductInfoStocksByWarehouseFBSRequest(
                        sku=["9876543210"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="product/info/stocks-by-warehouse/fbs",
            payload=request.model_dump(),
        )
        return ProductInfoStocksByWarehouseFBSResponse(**response)
