from ...core import APIManager
from ...schemas.products import ProductInfoDescriptionRequest, ProductInfoDescriptionResponse


class ProductInfoDescriptionMixin(APIManager):
    """Реализует метод /v1/product/info/description"""

    async def product_info_description(
        self: "ProductInfoDescriptionMixin",
        request: ProductInfoDescriptionRequest
    ) -> ProductInfoDescriptionResponse:
        """Получает название и описание товара по идентификатору.

        Notes:
            • Вы можете передать `product_id` или `offer_id`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/ProductAPI_GetProductInfoDescription

        Args:
            request: `product_id` или `offer_id` по схеме `ProductInfoDescriptionRequest`.

        Returns:
            Информация о товаре с названием и описанием по схеме `ProductInfoDescriptionResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_description(
                    ProductInfoDescriptionRequest(product_id=12345678)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/description",
            payload=request.model_dump(),
        )
        return ProductInfoDescriptionResponse(**response)
