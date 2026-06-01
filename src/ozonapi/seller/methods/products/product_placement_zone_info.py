from ...core import APIManager
from ...schemas.products import (
    ProductPlacementZoneInfoRequest,
    ProductPlacementZoneInfoResponse,
)


class ProductPlacementZoneInfoMixin(APIManager):
    """Реализует метод /v1/product/placement-zone/info"""

    async def product_placement_zone_info(
            self: "ProductPlacementZoneInfoMixin",
            request: ProductPlacementZoneInfoRequest,
    ) -> ProductPlacementZoneInfoResponse:
        """Метод для получения зон размещения товаров по SKU перед поставкой.

        Notes:
            • Возвращает зону размещения для каждого переданного SKU.
            • Известные значения зон: `UNSPECIFIED`, `CLOSED_ZONE`, `DANGEROUS_GOODS`,
              `PRODUCTS`, `SORT`, `NON_SORT`, `OVERSIZE`, `JEWELRY`, `UNRESOLVED`
              (набор может расширяться).

        References:
            https://docs.ozon.ru/api/seller/?#operation/ProductAPI_GetProductPlacementZoneInfo

        Args:
            request: Список SKU по схеме `ProductPlacementZoneInfoRequest`

        Returns:
            Список товаров с зонами размещения по схеме `ProductPlacementZoneInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_placement_zone_info(
                    ProductPlacementZoneInfoRequest(skus=["123456789"])
                )

            for item in result.products_placement:
                print(item.sku, item.placement_zone)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/placement-zone/info",
            payload=request.model_dump(),
        )
        return ProductPlacementZoneInfoResponse(**response)
