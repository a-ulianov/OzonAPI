from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductInfoWarehouseStocksRequest,
    ProductInfoWarehouseStocksResponse,
)


class ProductInfoWarehouseStocksMixin(APIManager):
    """Реализует метод /v1/product/info/warehouse/stocks"""

    async def product_info_warehouse_stocks(
            self: "ProductInfoWarehouseStocksMixin",
            request: ProductInfoWarehouseStocksRequest
    ) -> ProductInfoWarehouseStocksResponse:
        """Возвращает информацию по остаткам товаров на складе FBS и rFBS.

        Notes:
            • Курсорная пагинация: если `has_next` равно true, передайте полученный
              `cursor` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductInfoWarehouseStocks

        Args:
            request: Запрос по схеме `ProductInfoWarehouseStocksRequest`

        Returns:
            Остатки на складе по схеме `ProductInfoWarehouseStocksResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_warehouse_stocks(
                    ProductInfoWarehouseStocksRequest(warehouse_id=123, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/warehouse/stocks",
            payload=request.model_dump()
        )
        return ProductInfoWarehouseStocksResponse(**response)
