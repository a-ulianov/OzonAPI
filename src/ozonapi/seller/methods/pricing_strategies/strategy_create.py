from ...core import APIManager
from ...schemas.pricing_strategies import (
    StrategyCreateRequest,
    StrategyCreateResponse,
)


class StrategyCreateMixin(APIManager):
    """Реализует метод /v1/pricing-strategy/create"""

    async def strategy_create(
            self: "StrategyCreateMixin",
            request: StrategyCreateRequest,
    ) -> StrategyCreateResponse:
        """Создаёт новую стратегию ценообразования.

        Notes:
            • Стратегия может включать одного или нескольких конкурентов с коэффициентами.
            • Коэффициент задаёт, во сколько раз корректируется минимальная цена конкурента.
            • Допустимый диапазон коэффициента — от 0.5 до 1.2.
            • После создания стратегию необходимо активировать методом `strategy_status()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/pricing_create

        Args:
            request: Параметры новой стратегии по схеме `StrategyCreateRequest`

        Returns:
            Идентификатор созданной стратегии по схеме `StrategyCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.strategy_create(
                    StrategyCreateRequest(
                        strategy_name="Моя стратегия",
                        competitors=[
                            StrategyCompetitor(competitor_id=1, coefficient=1.0)
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pricing-strategy/create",
            payload=request.model_dump(),
        )
        return StrategyCreateResponse(**response)
