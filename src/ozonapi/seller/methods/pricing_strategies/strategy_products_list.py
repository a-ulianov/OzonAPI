from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyProductsListRequest,
    StrategyProductsListResponse,
)


class StrategyProductsListMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/products/list"""

    async def strategy_products_list(
            self: "StrategyProductsListMixin",
            request: StrategyProductsListRequest,
    ) -> StrategyProductsListResponse:
        """Возвращает список товаров, добавленных в стратегию ценообразования.

        Notes:
            • Возвращает идентификаторы товаров (`product_id`) в виде строк.
            • Для получения детальной информации о товарах используйте методы раздела Товары.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_items-list

        Args:
            request: Идентификатор стратегии по схеме `StrategyProductsListRequest`

        Returns:
            Список идентификаторов товаров по схеме `StrategyProductsListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_products_list(
                    StrategyProductsListRequest(strategy_id="abc123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/list",
            payload=request.model_dump(),
        )
        return StrategyProductsListResponse(**response)
