from ...core import APIManager
from ...schemas.reports import ReportListRequest, ReportListResponse


class ReportListMixin(APIManager):
    """Реализует метод /v1/report/list"""

    async def report_list(
            self: "ReportListMixin",
            request: ReportListRequest
    ) -> ReportListResponse:
        """Метод для получения списка отчётов.

        Notes:
            • Возвращает все сгенерированные отчёты с фильтрацией по типу.
            • Постраничный вывод через `page` и `page_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportList

        Args:
            request: Запрос на получение списка отчётов по схеме `ReportListRequest`

        Returns:
            Список отчётов по схеме `ReportListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_list(
                    ReportListRequest(
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/list",
            payload=request.model_dump()
        )
        return ReportListResponse(**response)
