from ...core import APIManager
from ...schemas.beta import (
    RemovalFromSupplyListRequest,
    RemovalFromSupplyListResponse,
)


class RemovalFromSupplyListMixin(APIManager):
    """Реализует метод /v1/removal/from-supply/list"""

    async def removal_from_supply_list(
            self: "RemovalFromSupplyListMixin",
            request: RemovalFromSupplyListRequest
    ) -> RemovalFromSupplyListResponse:
        """Возвращает отчёт по вывозу и утилизации товаров с поставки FBO.

        Notes:
            • Пагинация по `last_id`: передайте полученный `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetSupplyReturnsSummaryReport

        Args:
            request: Запрос по схеме `RemovalFromSupplyListRequest`

        Returns:
            Отчёт по схеме `RemovalFromSupplyListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.removal_from_supply_list(
                    RemovalFromSupplyListRequest(date_from="2026-05-01", date_to="2026-06-01", limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="removal/from-supply/list",
            payload=request.model_dump()
        )
        return RemovalFromSupplyListResponse(**response)
