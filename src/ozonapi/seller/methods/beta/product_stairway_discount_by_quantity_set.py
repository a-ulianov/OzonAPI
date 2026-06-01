from ...core import APIManager
from ...schemas.beta import (
    ProductStairwayDiscountByQuantitySetRequest,
    ProductStairwayDiscountByQuantitySetResponse,
)


class ProductStairwayDiscountByQuantitySetMixin(APIManager):
    """Реализует метод /v1/product/stairway-discount/by-quantity/set"""

    async def product_stairway_discount_by_quantity_set(
            self: "ProductStairwayDiscountByQuantitySetMixin",
            request: ProductStairwayDiscountByQuantitySetRequest
    ) -> ProductStairwayDiscountByQuantitySetResponse:
        """Управляет скидкой от количества (лестницей скидок) для товаров.

        Notes:
            • Передайте `suppress_warnings = true`, чтобы применить настройки несмотря
              на предупреждения.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_SetProductStairwayDiscountByQuantity

        Args:
            request: Запрос по схеме `ProductStairwayDiscountByQuantitySetRequest`

        Returns:
            Результат применения по схеме `ProductStairwayDiscountByQuantitySetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_stairway_discount_by_quantity_set(
                    ProductStairwayDiscountByQuantitySetRequest(
                        stairways=[{
                            "enabled": True,
                            "sku": 123,
                            "stairway": {"steps": [{"discount": 5, "quantity": 2, "step": 1}]},
                        }]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/stairway-discount/by-quantity/set",
            payload=request.model_dump()
        )
        return ProductStairwayDiscountByQuantitySetResponse(**response)
