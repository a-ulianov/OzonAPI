from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyCompetitorsListRequest,
    StrategyCompetitorsListResponse,
)


class StrategyCompetitorsListMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/competitors/list"""

    async def strategy_competitors_list(
            self: "StrategyCompetitorsListMixin",
            request: StrategyCompetitorsListRequest,
    ) -> StrategyCompetitorsListResponse:
        """Возвращает список доступных конкурентов для стратегий ценообразования.

        Notes:
            • Конкуренты — это торговые площадки, чьи цены отслеживает стратегия.
            • Постраничная выборка: минимальная страница — 1, максимум 50 записей на страницу.
            • Используйте `competitor_id` из ответа при создании или обновлении стратегии.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_competitors

        Args:
            request: Параметры постраничного запроса по схеме `StrategyCompetitorsListRequest`

        Returns:
            Список конкурентов и их общее количество по схеме `StrategyCompetitorsListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_competitors_list(
                    StrategyCompetitorsListRequest(page=1, limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/competitors/list",
            payload=request.model_dump(),
        )
        return StrategyCompetitorsListResponse(**response)
