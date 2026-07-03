from ...core import APIManager
from ...schemas.prices_and_stocks import ProductInfoStocksByWarehouseFBORequest, ProductInfoStocksByWarehouseFBOResponse


class ProductInfoStocksByWarehouseFBOMixin(APIManager):
    """Реализует метод /v1/product/info/stocks-by-warehouse/fbo"""

    async def product_info_stocks_by_warehouse_fbo(
        self: "ProductInfoStocksByWarehouseFBOMixin",
        request: ProductInfoStocksByWarehouseFBORequest
    ) -> ProductInfoStocksByWarehouseFBOResponse:
        """Метод для получения информации о складских остатках и зарезервированном кол-ве в разбивке по складам FBO.

        Notes:
            • Фильтровать можно по `skus` и/или `offer_ids`.
            • Курсорная пагинация: если `has_next` равно true, передайте полученный `cursor`
              в следующий запрос, чтобы получить оставшиеся остатки.
            • Метод в статусе beta (тег `BetaMethod`).

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocksByWarehouseFbo

        Args:
            request: Параметры запроса по схеме `ProductInfoStocksByWarehouseFBORequest`
                (limit, cursor, skus, offer_ids)

        Returns:
            Ответ с информацией об остатках и резерве по складам FBO
            по схеме `ProductInfoStocksByWarehouseFBOResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_stocks_by_warehouse_fbo(
                    ProductInfoStocksByWarehouseFBORequest(
                        skus=["9876543210"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbo",
            payload=request.model_dump(),
        )
        return ProductInfoStocksByWarehouseFBOResponse(**response)
