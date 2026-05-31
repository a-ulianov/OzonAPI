from ...core import APIManager
from ...schemas.reports import ReportDiscountedCreateResponse


class ReportDiscountedCreateMixin(APIManager):
    """Реализует метод /v1/report/discounted/create"""

    async def report_discounted_create(
            self: "ReportDiscountedCreateMixin"
    ) -> ReportDiscountedCreateResponse:
        """Метод для создания отчёта об уценённых товарах.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateDiscountedReport

        Returns:
            Код отчёта по схеме `ReportDiscountedCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_discounted_create()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/discounted/create",
            payload={}
        )
        return ReportDiscountedCreateResponse(**response)
