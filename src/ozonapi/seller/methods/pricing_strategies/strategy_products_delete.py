from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyProductsDeleteRequest,
    StrategyProductsDeleteResponse,
)


class StrategyProductsDeleteMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/products/delete"""

    async def strategy_products_delete(
            self: "StrategyProductsDeleteMixin",
            request: StrategyProductsDeleteRequest,
    ) -> StrategyProductsDeleteResponse:
        """Удаляет товары из стратегии ценообразования.

        Notes:
            • После удаления товары перестают участвовать в стратегии ценообразования.
            • `failed_product_count` в ответе показывает количество товаров, которые не удалось удалить.
            • Передавайте `product_id` в виде строк, даже если значения числовые.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_items-delete

        Args:
            request: Список идентификаторов товаров по схеме `StrategyProductsDeleteRequest`

        Returns:
            Результат удаления товаров по схеме `StrategyProductsDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_products_delete(
                    StrategyProductsDeleteRequest(
                        product_id=["123456789", "987654321"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/delete",
            payload=request.model_dump(),
        )
        return StrategyProductsDeleteResponse(**response)
