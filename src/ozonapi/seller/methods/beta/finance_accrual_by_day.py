from ...core import APIManager
from ...schemas.beta import (
    FinanceAccrualByDayRequest,
    FinanceAccrualByDayResponse,
)


class FinanceAccrualByDayMixin(APIManager):
    """Реализует метод /v1/finance/accrual/by-day"""

    async def finance_accrual_by_day(
            self: "FinanceAccrualByDayMixin",
            request: FinanceAccrualByDayRequest
    ) -> FinanceAccrualByDayResponse:
        """Возвращает начисления за указанный день.

        Notes:
            • Пагинация по `last_id`: передайте полученный `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualByDay

        Args:
            request: Запрос по схеме `FinanceAccrualByDayRequest`

        Returns:
            Начисления за день по схеме `FinanceAccrualByDayResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_accrual_by_day(
                    FinanceAccrualByDayRequest(date="2026-05-15")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/by-day",
            payload=request.model_dump()
        )
        return FinanceAccrualByDayResponse(**response)
