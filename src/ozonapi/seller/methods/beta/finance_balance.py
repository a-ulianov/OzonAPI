from ...core import APIManager
from ...schemas.beta import FinanceBalanceRequest, FinanceBalanceResponse


class FinanceBalanceMixin(APIManager):
    """Реализует метод /v1/finance/balance"""

    async def finance_balance(
            self: "FinanceBalanceMixin",
            request: FinanceBalanceRequest
    ) -> FinanceBalanceResponse:
        """Возвращает отчёт о балансе за указанный период.

        Notes:
            • Период задаётся полями `date_from` и `date_to` в формате YYYY-MM-DD
              (не более 3 месяцев).

        References:
            https://docs.ozon.ru/api/seller/#operation/GetFinanceBalanceV1

        Args:
            request: Запрос по схеме `FinanceBalanceRequest`

        Returns:
            Отчёт о балансе по схеме `FinanceBalanceResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_balance(
                    FinanceBalanceRequest(date_from="2026-05-01", date_to="2026-06-01")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/balance",
            payload=request.model_dump()
        )
        return FinanceBalanceResponse(**response)
