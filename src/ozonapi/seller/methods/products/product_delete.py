from ...core import APIManager
from ...schemas.products import ProductsDeleteRequest, ProductsDeleteResponse


class ProductDeleteMixin(APIManager):
    """Реализует метод /v2/products/delete"""

    async def products_delete(
        self: "ProductDeleteMixin",
        request: ProductsDeleteRequest
    ) -> ProductsDeleteResponse:
        """Удаляет архивные товары без SKU из системы Ozon.

        Notes:
            • В одном запросе можно передать до `500` идентификаторов товаров.
            • Удалить можно только товары без SKU из архива.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_DeleteProducts

        Args:
            request: Список товаров для удаления по схеме `ProductsDeleteRequest`.

        Returns:
            Статус обработки запроса для каждого товара по схеме `ProductsDeleteResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.products_delete(
                    ProductsDeleteRequest(
                        products=[
                            ProductDeleteRequestItem(offer_id="033"),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="products/delete",
            payload=request.model_dump(),
        )
        return ProductsDeleteResponse(**response)
