from ...core import APIManager
from ...schemas.products import ProductRelatedSkuGetRequest, ProductRelatedSkuGetResponse


class ProductRelatedSkuGetMixin(APIManager):
    """Реализует метод /v1/product/related-sku/get"""

    async def product_related_sku_get(
        self: "ProductRelatedSkuGetMixin",
        request: ProductRelatedSkuGetRequest
    ) -> ProductRelatedSkuGetResponse:
        """Получает единый SKU по старым идентификаторам SKU FBS и SKU FBO.

        Notes:
            • В ответе возвращаются все SKU, связанные с переданными.
            • Метод может обработать любые SKU, даже скрытые или удалённые.
            • В одном запросе можно передать до 200 SKU.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductGetRelatedSKU

        Args:
            request: Список SKU для получения связанных идентификаторов по схеме `ProductRelatedSkuGetRequest`.

        Returns:
            Информация о связанных SKU и возможные ошибки обработки по схеме `ProductRelatedSkuGetResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_related_sku_get(
                    ProductRelatedSkuGetRequest(
                        sku=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/related-sku/get",
            payload=request.model_dump(),
        )
        return ProductRelatedSkuGetResponse(**response)
