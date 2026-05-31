from ...core import APIManager
from ...schemas.reports import ReportInfoRequest, ReportInfoResponse


class ReportInfoMixin(APIManager):
    """Реализует метод /v1/report/info"""

    async def report_info(
            self: "ReportInfoMixin",
            request: ReportInfoRequest
    ) -> ReportInfoResponse:
        """Метод для получения информации об отчёте.

        Notes:
            • Возвращает статус генерации отчёта и ссылку на файл по его коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportInfo

        Args:
            request: Запрос на получение информации об отчёте по схеме `ReportInfoRequest`

        Returns:
            Информация об отчёте по схеме `ReportInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_info(
                    ReportInfoRequest(
                        code="report-code"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/info",
            payload=request.model_dump()
        )
        return ReportInfoResponse(**response)
