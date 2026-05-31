from ...core import APIManager
from ...schemas.reports import (
    ReportPlacementBySuppliesCreateRequest,
    ReportPlacementBySuppliesCreateResponse,
)


class ReportPlacementBySuppliesCreateMixin(APIManager):
    """Реализует метод /v1/report/placement/by-supplies/create"""

    async def report_placement_by_supplies_create(
            self: "ReportPlacementBySuppliesCreateMixin",
            request: ReportPlacementBySuppliesCreateRequest
    ) -> ReportPlacementBySuppliesCreateResponse:
        """Метод для получения отчёта о стоимости размещения по поставкам.

        Notes:
            • Запускает асинхронную генерацию отчёта; статус — `report_info()` по коду.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreatePlacementBySuppliesReport

        Args:
            request: Запрос на создание отчёта по схеме `ReportPlacementBySuppliesCreateRequest`

        Returns:
            Код отчёта по схеме `ReportPlacementBySuppliesCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.report_placement_by_supplies_create(
                    ReportPlacementBySuppliesCreateRequest(
                        date_from="2026-01-01",
                        date_to="2026-02-01"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="report/placement/by-supplies/create",
            payload=request.model_dump()
        )
        return ReportPlacementBySuppliesCreateResponse(**response)
