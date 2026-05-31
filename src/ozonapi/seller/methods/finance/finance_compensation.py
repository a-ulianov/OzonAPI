from ...core import APIManager
from ...schemas.finance import (
    FinanceCompensationRequest,
    FinanceCompensationResponse,
)


class FinanceCompensationMixin(APIManager):
    """Реализует метод /v1/finance/compensation"""

    async def finance_compensation(
            self: "FinanceCompensationMixin",
            request: FinanceCompensationRequest
    ) -> FinanceCompensationResponse:
        """Запускает формирование отчёта о компенсациях.

        Notes:
            • Возвращает код отчёта; готовый документ доступен после генерации.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_CreateCompensationReport

        Args:
            request: Запрос на создание отчёта по схеме `FinanceCompensationRequest`

        Returns:
            Код отчёта по схеме `FinanceCompensationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_compensation(
                    FinanceCompensationRequest(date="2026-04", language="DEFAULT")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/compensation",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceCompensationResponse(**response)
