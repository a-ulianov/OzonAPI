from ...core import APIManager
from ...schemas.reports import (
    ReportProductsCreateRequest,
    ReportProductsCreateResponse,
)


class ReportProductsCreateMixin(APIManager):
    """Реализует метод /v1/report/products/create"""

    async def report_products_create(
            self: "ReportProductsCreateMixin",
            request: ReportProductsCreateRequest
    ) -> ReportProductsCreateResponse:
        """Метод для создания отчёта по товарам.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyProductsReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportProductsCreateRequest`

        Returns:
            Код отчёта по схеме `ReportProductsCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_products_create(
                    ReportProductsCreateRequest(
                        language="DEFAULT"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/products/create",
            payload=request.model_dump()
        )
        return ReportProductsCreateResponse(**response)
