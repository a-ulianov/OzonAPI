from ...core import APIManager
from ...schemas.reports import (
    ReportRealizationPostingCreateRequest,
    ReportRealizationPostingCreateResponse,
)


class ReportRealizationPostingCreateMixin(APIManager):
    """Реализует метод /v1/report/realization/posting/create"""

    async def report_realization_posting_create(
            self: "ReportRealizationPostingCreateMixin",
            request: ReportRealizationPostingCreateRequest
    ) -> ReportRealizationPostingCreateResponse:
        """Метод для создания позаказного отчёта о реализации товаров.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.
            • Отчёт формируется за календарный месяц: параметры `month` и `year`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyFinanceRealizationPostingReport

        Args:
            request: Запрос на создание отчёта по схеме
                `ReportRealizationPostingCreateRequest`

        Returns:
            Код отчёта по схеме `ReportRealizationPostingCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_realization_posting_create(
                    ReportRealizationPostingCreateRequest(month=5, year=2026)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/realization/posting/create",
            payload=request.model_dump()
        )
        return ReportRealizationPostingCreateResponse(**response)
