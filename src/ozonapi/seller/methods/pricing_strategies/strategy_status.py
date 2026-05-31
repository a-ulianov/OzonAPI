from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyStatusRequest,
    StrategyStatusResponse,
)


class StrategyStatusMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/status"""

    async def strategy_status(
            self: "StrategyStatusMixin",
            request: StrategyStatusRequest,
    ) -> StrategyStatusResponse:
        """Изменяет статус стратегии ценообразования (включает или отключает).

        Notes:
            • `enabled=true` активирует стратегию, `enabled=false` — останавливает.
            • Остановленная стратегия не обновляет цены товаров.
            • При возобновлении стратегии цены обновятся при следующем цикле расчёта.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_status

        Args:
            request: Идентификатор стратегии и новый статус по схеме `StrategyStatusRequest`

        Returns:
            Пустой объект при успешном изменении статуса по схеме `StrategyStatusResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_status(
                    StrategyStatusRequest(strategy_id="abc123", enabled=True)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/status",
            payload=request.model_dump(),
        )
        return StrategyStatusResponse(**response)
