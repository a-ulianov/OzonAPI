from ...core import APIManager
from ...schemas.prices_and_stocks import ProductInfoStocksByWarehouseFBSRequest, ProductInfoStocksByWarehouseFBSResponse


class ProductInfoStocksByWarehouseFBSMixin(APIManager):
    """Реализует метод /v1/product/info/stocks-by-warehouse/fbs"""

    async def product_info_stocks_by_warehouse_fbs(
        self: "ProductInfoStocksByWarehouseFBSMixin",
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
            payload=request.model_dump(),
        )
        return ProductInfoStocksByWarehouseFBSResponse(**response)
