from ...core import APIManager
from ...schemas.beta import (
    ProductStairwayDiscountByQuantityGetRequest,
    ProductStairwayDiscountByQuantityGetResponse,
)


class ProductStairwayDiscountByQuantityGetMixin(APIManager):
    """Реализует метод /v1/product/stairway-discount/by-quantity/get"""

    async def product_stairway_discount_by_quantity_get(
            self: "ProductStairwayDiscountByQuantityGetMixin",
            request: ProductStairwayDiscountByQuantityGetRequest
    ) -> ProductStairwayDiscountByQuantityGetResponse:
        """Возвращает информацию о скидке от количества (лестнице скидок) для товаров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductStairwayDiscountByQuantity

        Args:
            request: Запрос по схеме `ProductStairwayDiscountByQuantityGetRequest`

        Returns:
            Настройки скидок по схеме `ProductStairwayDiscountByQuantityGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_stairway_discount_by_quantity_get(
                    ProductStairwayDiscountByQuantityGetRequest(skus=["123456789"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/stairway-discount/by-quantity/get",
            payload=request.model_dump()
        )
        return ProductStairwayDiscountByQuantityGetResponse(**response)
