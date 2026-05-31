from ...core import APIManager
from ...schemas.finance import (
    FinanceRealizationPostingRequest,
    FinanceRealizationPostingResponse,
)


class FinanceRealizationPostingMixin(APIManager):
    """Реализует метод /v1/finance/realization/posting"""

    async def finance_realization_posting(
            self: "FinanceRealizationPostingMixin",
            request: FinanceRealizationPostingRequest
    ) -> FinanceRealizationPostingResponse:
        """Возвращает отчёт о реализации товаров в разрезе отправлений.

        Notes:
            • В отличие от `finance_realization`, каждая строка содержит данные об
              отправлении (`order`) и документе юридического лица.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceRealizationPostingV1

        Args:
            request: Запрос отчёта по схеме `FinanceRealizationPostingRequest`

        Returns:
            Отчёт о реализации по схеме `FinanceRealizationPostingResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_realization_posting(
                    FinanceRealizationPostingRequest(month=4, year=2026)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/realization/posting",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceRealizationPostingResponse(**response)
