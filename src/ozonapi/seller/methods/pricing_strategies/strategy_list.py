from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyListRequest,
    StrategyListResponse,
)


class StrategyListMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/list"""

    async def strategy_list(
            self: "StrategyListMixin",
            request: StrategyListRequest,
    ) -> StrategyListResponse:
        """Возвращает постраничный список стратегий ценообразования продавца.

        Notes:
            • Максимальное количество записей на странице — 50.
            • Нумерация страниц начинается с 1.
            • Для каждой стратегии возвращается количество товаров и конкурентов.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_list

        Args:
            request: Параметры постраничного запроса по схеме `StrategyListRequest`

        Returns:
            Список стратегий и их общее количество по схеме `StrategyListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_list(
                    StrategyListRequest(page=1, limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/list",
            payload=request.model_dump(),
        )
        return StrategyListResponse(**response)
