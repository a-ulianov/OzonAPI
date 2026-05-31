from ...core import APIManager
from ...schemas.finance import (
    FinanceRealizationRequest,
    FinanceRealizationResponse,
)


class FinanceRealizationMixin(APIManager):
    """Реализует метод /v2/finance/realization"""

    async def finance_realization(
            self: "FinanceRealizationMixin",
            request: FinanceRealizationRequest
    ) -> FinanceRealizationResponse:
        """Возвращает отчёт о реализации товаров за указанный месяц.

        Notes:
            • Отчёт содержит заголовок (реквизиты сторон) и построчную детализацию
              по товарам с комиссиями за доставку и возврат.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceRealizationV2

        Args:
            request: Запрос отчёта по схеме `FinanceRealizationRequest`

        Returns:
            Отчёт о реализации по схеме `FinanceRealizationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_realization(
                    FinanceRealizationRequest(month=4, year=2026)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="finance/realization",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceRealizationResponse(**response)
