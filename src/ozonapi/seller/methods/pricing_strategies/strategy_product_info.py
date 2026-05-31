from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyProductInfoRequest,
    StrategyProductInfoResponse,
)


class StrategyProductInfoMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/product/info"""

    async def strategy_product_info(
            self: "StrategyProductInfoMixin",
            request: StrategyProductInfoRequest,
    ) -> StrategyProductInfoResponse:
        """Возвращает информацию о цене товара по стратегии ценообразования.

        Notes:
            • Возвращает текущую цену по стратегии и ссылку на товар конкурента.
            • `is_enabled` показывает, участвует ли товар в активной стратегии.
            • `strategy_competitor_id` — устаревшее поле, рекомендуется использовать URL конкурента.
            • `price_downloaded_at` — дата последнего обновления цены по стратегии.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_items-info

        Args:
            request: Идентификатор товара по схеме `StrategyProductInfoRequest`

        Returns:
            Информация о цене товара по стратегии по схеме `StrategyProductInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_product_info(
                    StrategyProductInfoRequest(product_id=123456789)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/product/info",
            payload=request.model_dump(),
        )
        return StrategyProductInfoResponse(**response)
