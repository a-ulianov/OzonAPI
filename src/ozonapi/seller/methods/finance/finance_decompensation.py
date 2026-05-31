from ...core import APIManager
from ...schemas.finance import (
    FinanceDecompensationRequest,
    FinanceDecompensationResponse,
)


class FinanceDecompensationMixin(APIManager):
    """Реализует метод /v1/finance/decompensation"""

    async def finance_decompensation(
            self: "FinanceDecompensationMixin",
            request: FinanceDecompensationRequest
    ) -> FinanceDecompensationResponse:
        """Запускает формирование отчёта о декомпенсациях.

        Notes:
            • Возвращает код отчёта; готовый документ доступен после генерации.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_CreateDecompensationReport

        Args:
            request: Запрос на создание отчёта по схеме `FinanceDecompensationRequest`

        Returns:
            Код отчёта по схеме `FinanceDecompensationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_decompensation(
                    FinanceDecompensationRequest(date="2026-04", language="DEFAULT")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/decompensation",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceDecompensationResponse(**response)
