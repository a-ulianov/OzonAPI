from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyIdsByProductIdsRequest,
    StrategyIdsByProductIdsResponse,
)


class StrategyIdsByProductIdsMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/strategy-ids-by-product-ids"""

    async def strategy_ids_by_product_ids(
            self: "StrategyIdsByProductIdsMixin",
            request: StrategyIdsByProductIdsRequest,
    ) -> StrategyIdsByProductIdsResponse:
        """Возвращает идентификаторы стратегий по идентификаторам товаров.

        Notes:
            • Позволяет определить, к каким стратегиям привязаны переданные товары.
            • Передавайте `product_id` в виде строк, даже если значения числовые.
            • Если товар не привязан ни к одной стратегии, он не попадёт в ответ.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_ids

        Args:
            request: Список идентификаторов товаров по схеме `StrategyIdsByProductIdsRequest`

        Returns:
            Связи товаров со стратегиями по схеме `StrategyIdsByProductIdsResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_ids_by_product_ids(
                    StrategyIdsByProductIdsRequest(
                        product_id=["123456789", "987654321"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/strategy-ids-by-product-ids",
            payload=request.model_dump(),
        )
        return StrategyIdsByProductIdsResponse(**response)
