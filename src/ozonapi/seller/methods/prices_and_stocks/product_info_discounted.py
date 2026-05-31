from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductInfoDiscountedRequest,
    ProductInfoDiscountedResponse,
)


class ProductInfoDiscountedMixin(APIManager):
    """Реализует метод /v1/product/info/discounted"""

    async def product_info_discounted(
            self: "ProductInfoDiscountedMixin",
            request: ProductInfoDiscountedRequest,
    ) -> ProductInfoDiscountedResponse:
        """Получает информацию об уценке и основном товаре по SKU уценённого товара.

        Notes:
            • Метод возвращает условия уценки: состояние товара, дефекты, повреждения упаковки и т. д.
            • Для каждого уценённого товара возвращается SKU основного товара (`sku`).
            • `condition_estimation` — состояние товара по шкале от 1 (удовлетворительное) до 7 (как новый).
            • Передавайте SKU именно уценённых товаров, а не основных.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoDiscounted

        Args:
            request: SKU уценённых товаров по схеме `ProductInfoDiscountedRequest`

        Returns:
            Информация об уценке и основном товаре по схеме `ProductInfoDiscountedResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_discounted(
                    ProductInfoDiscountedRequest(
                        discounted_skus=["635548518"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/discounted",
            payload=request.model_dump(),
        )
        return ProductInfoDiscountedResponse(**response)
