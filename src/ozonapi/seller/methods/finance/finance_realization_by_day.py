from ...core import APIManager
from ...schemas.finance import (
    FinanceRealizationByDayRequest,
    FinanceRealizationByDayResponse,
)


class FinanceRealizationByDayMixin(APIManager):
    """Реализует метод /v1/finance/realization/by-day"""

    async def finance_realization_by_day(
            self: "FinanceRealizationByDayMixin",
            request: FinanceRealizationByDayRequest,
    ) -> FinanceRealizationByDayResponse:
        """Возвращает отчёт о реализации товаров за указанный день (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Дата задаётся отдельными полями `day`, `month`, `year`.
            • Каждая строка отчёта содержит товар и начисления по доставленным
              (`delivery_commission`) и возвращённым (`return_commission`) товарам.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetRealizationByDayReportV1

        Args:
            request: Дата отчёта по схеме `FinanceRealizationByDayRequest`

        Returns:
            Отчёт о реализации за день по схеме `FinanceRealizationByDayResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_realization_by_day(
                    FinanceRealizationByDayRequest(day=1, month=6, year=2026)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/realization/by-day",
            payload=request.model_dump(),
        )
        return FinanceRealizationByDayResponse(**response)
