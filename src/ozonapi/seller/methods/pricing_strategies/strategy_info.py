from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyInfoRequest,
    StrategyInfoResponse,
)


class StrategyInfoMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/info"""

    async def strategy_info(
            self: "StrategyInfoMixin",
            request: StrategyInfoRequest,
    ) -> StrategyInfoResponse:
        """Возвращает детальную информацию о стратегии ценообразования.

        Notes:
            • Возвращает список конкурентов с их коэффициентами, статус и тип стратегии.
            • Поле `type`: MIN_EXT_PRICE — системная стратегия, COMP_PRICE — пользовательская.
            • Поле `update_type` отражает последнее изменение стратегии.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_info

        Args:
            request: Идентификатор стратегии по схеме `StrategyInfoRequest`

        Returns:
            Детальная информация о стратегии по схеме `StrategyInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_info(
                    StrategyInfoRequest(strategy_id="abc123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/info",
            payload=request.model_dump(),
        )
        return StrategyInfoResponse(**response)
