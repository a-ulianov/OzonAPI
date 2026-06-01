from ...core import APIManager
from ...schemas.beta import (
    FinanceAccrualTypesRequest,
    FinanceAccrualTypesResponse,
)


class FinanceAccrualTypesMixin(APIManager):
    """Реализует метод /v1/finance/accrual/types"""

    async def finance_accrual_types(
            self: "FinanceAccrualTypesMixin",
            request: FinanceAccrualTypesRequest
    ) -> FinanceAccrualTypesResponse:
        """Возвращает справочник типов начислений.

        Notes:
            • Запрос без параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetFinanceAccrualTypes

        Args:
            request: Запрос по схеме `FinanceAccrualTypesRequest`

        Returns:
            Справочник начислений по схеме `FinanceAccrualTypesResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_accrual_types(FinanceAccrualTypesRequest())
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/accrual/types",
            payload=request.model_dump()
        )
        return FinanceAccrualTypesResponse(**response)
