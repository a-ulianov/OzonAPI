from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyProductsAddRequest,
    StrategyProductsAddResponse,
)


class StrategyProductsAddMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/products/add"""

    async def strategy_products_add(
            self: "StrategyProductsAddMixin",
            request: StrategyProductsAddRequest,
    ) -> StrategyProductsAddResponse:
        """Добавляет товары в стратегию ценообразования.

        Notes:
            • Передавайте `product_id` в виде строк, даже если значения числовые.
            • При ошибке для отдельных товаров остальные добавляются успешно.
            • Список ошибок и количество неудачных добавлений возвращаются в `result.errors`.
            • Товар может быть привязан только к одной стратегии одновременно.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_items-add

        Args:
            request: Список товаров и идентификатор стратегии по схеме `StrategyProductsAddRequest`

        Returns:
            Результат добавления товаров по схеме `StrategyProductsAddResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_products_add(
                    StrategyProductsAddRequest(
                        strategy_id="abc123",
                        product_id=["123456789", "987654321"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/products/add",
            payload=request.model_dump(),
        )
        return StrategyProductsAddResponse(**response)
