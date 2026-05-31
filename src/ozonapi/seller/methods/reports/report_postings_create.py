from ...core import APIManager
from ...schemas.reports import (
    ReportPostingsCreateRequest,
    ReportPostingsCreateResponse,
)


class ReportPostingsCreateMixin(APIManager):
    """Реализует метод /v1/report/postings/create"""

    async def report_postings_create(
            self: "ReportPostingsCreateMixin",
            request: ReportPostingsCreateRequest
    ) -> ReportPostingsCreateResponse:
        """Метод для создания отчёта об отправлениях.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyPostingsReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportPostingsCreateRequest`

        Returns:
            Код отчёта по схеме `ReportPostingsCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_postings_create(
                    ReportPostingsCreateRequest(
                        filter=ReportPostingsCreateFilter(delivery_schema=["FBS"])
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/postings/create",
            payload=request.model_dump(by_alias=True)
        )
        return ReportPostingsCreateResponse(**response)
