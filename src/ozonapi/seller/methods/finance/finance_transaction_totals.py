from ...core import APIManager
from ...schemas.finance import (
    FinanceTransactionTotalsRequest,
    FinanceTransactionTotalsResponse,
)


class FinanceTransactionTotalsMixin(APIManager):
    """Реализует метод /v3/finance/transaction/totals"""

    async def finance_transaction_totals(
            self: "FinanceTransactionTotalsMixin",
            request: FinanceTransactionTotalsRequest
    ) -> FinanceTransactionTotalsResponse:
        """Возвращает итоговые суммы по транзакциям за период.

        Notes:
            • Агрегирует начисления: стоимость товаров, комиссии, доставку, компенсации
              и прочие суммы за указанный период или по отправлению.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceTransactionTotalsV3

        Args:
            request: Запрос итогов по схеме `FinanceTransactionTotalsRequest`

        Returns:
            Итоговые суммы по схеме `FinanceTransactionTotalsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_transaction_totals(
                    FinanceTransactionTotalsRequest(
                        date=FinancePeriod(from_="2026-04-01T00:00:00.000Z",
                                           to="2026-04-30T23:59:59.999Z")
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="finance/transaction/totals",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceTransactionTotalsResponse(**response)
