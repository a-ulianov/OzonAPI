from ...core import APIManager
from ...schemas.finance import (
    FinanceMutualSettlementRequest,
    FinanceMutualSettlementResponse,
)


class FinanceMutualSettlementMixin(APIManager):
    """Реализует метод /v1/finance/mutual-settlement"""

    async def finance_mutual_settlement(
            self: "FinanceMutualSettlementMixin",
            request: FinanceMutualSettlementRequest
    ) -> FinanceMutualSettlementResponse:
        """Запускает формирование отчёта о взаиморасчётах.

        Notes:
            • Возвращает код отчёта; готовый документ доступен после генерации.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_CreateMutualSettlementReport

        Args:
            request: Запрос на создание отчёта по схеме `FinanceMutualSettlementRequest`

        Returns:
            Код отчёта по схеме `FinanceMutualSettlementResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_mutual_settlement(
                    FinanceMutualSettlementRequest(date="2026-04", language="DEFAULT")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/mutual-settlement",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceMutualSettlementResponse(**response)
