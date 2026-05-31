from ...core import APIManager
from ...schemas.reports import (
    ReportPlacementByProductsCreateRequest,
    ReportPlacementByProductsCreateResponse,
)


class ReportPlacementByProductsCreateMixin(APIManager):
    """Реализует метод /v1/report/placement/by-products/create"""

    async def report_placement_by_products_create(
            self: "ReportPlacementByProductsCreateMixin",
            request: ReportPlacementByProductsCreateRequest
    ) -> ReportPlacementByProductsCreateResponse:
        """Метод для получения отчёта о стоимости размещения по товарам.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreatePlacementByProductsReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportPlacementByProductsCreateRequest`

        Returns:
            Код отчёта по схеме `ReportPlacementByProductsCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_placement_by_products_create(
                    ReportPlacementByProductsCreateRequest(
                        date_from="2026-01-01",
                        date_to="2026-02-01"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/placement/by-products/create",
            payload=request.model_dump()
        )
        return ReportPlacementByProductsCreateResponse(**response)
