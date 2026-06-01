from ...core import APIManager
from ...schemas.beta import (
    ProductVisibilitySetRequest,
    ProductVisibilitySetResponse,
)


class ProductVisibilitySetMixin(APIManager):
    """Реализует метод /v1/product/visibility/set"""

    async def product_visibility_set(
            self: "ProductVisibilitySetMixin",
            request: ProductVisibilitySetRequest
    ) -> ProductVisibilitySetResponse:
        """Настраивает видимость товара на витринах Ozon и Ozon Селект.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductVisibilitySet

        Args:
            request: Запрос по схеме `ProductVisibilitySetRequest`

        Returns:
            Результат настройки по схеме `ProductVisibilitySetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_visibility_set(
                    ProductVisibilitySetRequest(
                        item_placement=[{"placement": "OZON_SELECT", "sku": 123}]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/visibility/set",
            payload=request.model_dump()
        )
        return ProductVisibilitySetResponse(**response)
