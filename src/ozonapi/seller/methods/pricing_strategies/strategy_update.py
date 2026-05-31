from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyUpdateRequest,
    StrategyUpdateResponse,
)


class StrategyUpdateMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/update"""

    async def strategy_update(
            self: "StrategyUpdateMixin",
            request: StrategyUpdateRequest,
    ) -> StrategyUpdateResponse:
        """Обновляет параметры существующей стратегии ценообразования.

        Notes:
            • Обновляет название стратегии и список конкурентов с коэффициентами.
            • Коэффициент задаёт, во сколько раз корректируется минимальная цена конкурента.
            • Допустимый диапазон коэффициента — от 0.5 до 1.2.
            • Полностью заменяет список конкурентов — передавайте полный актуальный список.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_update

        Args:
            request: Обновлённые параметры стратегии по схеме `StrategyUpdateRequest`

        Returns:
            Пустой объект при успешном обновлении по схеме `StrategyUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_update(
                    StrategyUpdateRequest(
                        strategy_id="abc123",
                        strategy_name="Обновлённая стратегия",
                        competitors=[
                            StrategyCompetitor(competitor_id=1, coefficient=0.95)
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/update",
            payload=request.model_dump(),
        )
        return StrategyUpdateResponse(**response)
