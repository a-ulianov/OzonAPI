from ...core import APIManager
from ...schemas.reports import (
    ReportMarkedProductsSalesCreateRequest,
    ReportMarkedProductsSalesCreateResponse,
)


class ReportMarkedProductsSalesCreateMixin(APIManager):
    """Реализует метод /v1/report/marked-products-sales/create"""

    async def report_marked_products_sales_create(
            self: "ReportMarkedProductsSalesCreateMixin",
            request: ReportMarkedProductsSalesCreateRequest
    ) -> ReportMarkedProductsSalesCreateResponse:
        """Метод для генерации отчёта по продажам товаров с маркировкой.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateMarkedProductsSalesReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportMarkedProductsSalesCreateRequest`

        Returns:
            Код отчёта по схеме `ReportMarkedProductsSalesCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_marked_products_sales_create(
                    ReportMarkedProductsSalesCreateRequest(
                        date=ReportMarkedProductsSalesCreateDate(from_="2026-01-01", to="2026-02-01")
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/marked-products-sales/create",
            payload=request.model_dump(by_alias=True)
        )
        return ReportMarkedProductsSalesCreateResponse(**response)
