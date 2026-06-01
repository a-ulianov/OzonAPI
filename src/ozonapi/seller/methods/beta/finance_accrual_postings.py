from ...core import APIManager
from ...schemas.beta import (
    FinanceAccrualPostingsRequest,
    FinanceAccrualPostingsResponse,
)


class FinanceAccrualPostingsMixin(APIManager):
    """Реализует метод /v1/finance/accrual/postings"""

    async def finance_accrual_postings(
            self: "FinanceAccrualPostingsMixin",
            request: FinanceAccrualPostingsRequest
    ) -> FinanceAccrualPostingsResponse:
        """Возвращает начисления по указанным отправлениям.

        Notes:
            • Справочник типов начислений (`type_id`) — методом `finance_accrual_types()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualPostings

        Args:
            request: Запрос по схеме `FinanceAccrualPostingsRequest`

        Returns:
            Начисления по отправлениям по схеме `FinanceAccrualPostingsResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_accrual_postings(
                    FinanceAccrualPostingsRequest(posting_numbers=["0001-1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/postings",
            payload=request.model_dump()
        )
        return FinanceAccrualPostingsResponse(**response)
