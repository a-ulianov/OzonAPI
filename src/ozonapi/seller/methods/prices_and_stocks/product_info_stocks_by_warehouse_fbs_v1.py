from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductInfoStocksByWarehouseFBSV1Request,
    ProductInfoStocksByWarehouseFBSV1Response,
)


class ProductInfoStocksByWarehouseFBSV1Mixin(APIManager):
    """Реализует метод /v1/product/info/stocks-by-warehouse/fbs"""

    async def product_info_stocks_by_warehouse_fbs_v1(
            self: "ProductInfoStocksByWarehouseFBSV1Mixin",
            request: ProductInfoStocksByWarehouseFBSV1Request
    ) -> ProductInfoStocksByWarehouseFBSV1Response:
        """Возвращает информацию об остатках на складах продавца (FBS и rFBS), API v1.

        Notes:
            • Устаревшая версия: используйте каноническую `product_info_stocks_by_warehouse_fbs()`
              (v2) с курсорной пагинацией.
            • Укажите `sku` и/или `offer_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbs

        Args:
            request: Запрос по схеме `ProductInfoStocksByWarehouseFBSV1Request`

        Returns:
            Остатки по складам по схеме `ProductInfoStocksByWarehouseFBSV1Response`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_stocks_by_warehouse_fbs_v1(
                    ProductInfoStocksByWarehouseFBSV1Request(sku=["9876543210"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            payload=request.model_dump()
        )
        return ProductInfoStocksByWarehouseFBSV1Response(**response)
