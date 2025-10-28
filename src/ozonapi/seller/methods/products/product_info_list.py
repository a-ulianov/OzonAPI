from ...core import APIManager
from ...schemas.products import ProductInfoListRequest, ProductInfoListResponse


class ProductInfoListMixin(APIManager):
    """Реализует метод /v3/product/info/list"""

    async def product_info_list(
        self: "ProductInfoListMixin",
        request: ProductInfoListRequest
    ) -> ProductInfoListResponse:
        """Получает информацию о товарах по их идентификаторам.

        Notes:
            • В запросе можно использовать что-то одно - либо `offer_id`, либо `product_id`, либо `sku`.
            • В одном запросе можно передать не больше `1000` идентификаторов.
            • 12 ноября 2025 отключим параметр `marketing_price` в ответе метода.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductInfoList

        Args:
            request: Идентификаторы товаров для получения информации по схеме `ProductInfoListRequest`.

        Returns:
            Информация о товарах по схеме `ProductInfoListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_list(
                    ProductInfoListRequest(
                        product_id=[123456789, 987654321],
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/info/list",
            payload=request.model_dump(),
        )
        return ProductInfoListResponse(**response)
