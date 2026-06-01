from ...core import APIManager
from ...schemas.beta import (
    ProductVisibilityInfoRequest,
    ProductVisibilityInfoResponse,
)


class ProductVisibilityInfoMixin(APIManager):
    """Реализует метод /v1/product/visibility/info"""

    async def product_visibility_info(
            self: "ProductVisibilityInfoMixin",
            request: ProductVisibilityInfoRequest
    ) -> ProductVisibilityInfoResponse:
        """Возвращает информацию о видимости товаров на витринах.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductVisibilityInfo

        Args:
            request: Запрос по схеме `ProductVisibilityInfoRequest`

        Returns:
            Информация о видимости по схеме `ProductVisibilityInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_visibility_info(
                    ProductVisibilityInfoRequest(skus=["123456789"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/visibility/info",
            payload=request.model_dump()
        )
        return ProductVisibilityInfoResponse(**response)
