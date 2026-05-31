from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyDeleteRequest,
    StrategyDeleteResponse,
)


class StrategyDeleteMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/delete"""

    async def strategy_delete(
            self: "StrategyDeleteMixin",
            request: StrategyDeleteRequest,
    ) -> StrategyDeleteResponse:
        """Удаляет стратегию ценообразования.

        Notes:
            • Перед удалением рекомендуется остановить стратегию методом `strategy_status()`.
            • После удаления все товары, привязанные к стратегии, теряют связь с ней.
            • Операция необратима.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_delete

        Args:
            request: Идентификатор удаляемой стратегии по схеме `StrategyDeleteRequest`

        Returns:
            Пустой объект при успешном удалении по схеме `StrategyDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_delete(
                    StrategyDeleteRequest(strategy_id="abc123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/delete",
            payload=request.model_dump(),
        )
        return StrategyDeleteResponse(**response)
