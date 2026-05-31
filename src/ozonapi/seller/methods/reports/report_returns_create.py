from ...core import APIManager
from ...schemas.reports import (
    ReportReturnsCreateRequest,
    ReportReturnsCreateResponse,
)


class ReportReturnsCreateMixin(APIManager):
    """Реализует метод /v2/report/returns/create"""

    async def report_returns_create(
            self: "ReportReturnsCreateMixin",
            request: ReportReturnsCreateRequest
    ) -> ReportReturnsCreateResponse:
        """Метод для создания отчёта о возвратах (версия 2).

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateReturnsReportV2

        Args:
            request: Запрос на создание отчёта по схеме `ReportReturnsCreateRequest`

        Returns:
            Код отчёта по схеме `ReportReturnsCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_returns_create(
                    ReportReturnsCreateRequest(
                        filter=ReportReturnsCreateFilter(delivery_schema="FBS")
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="report/returns/create",
            payload=request.model_dump()
        )
        return ReportReturnsCreateResponse(**response)
