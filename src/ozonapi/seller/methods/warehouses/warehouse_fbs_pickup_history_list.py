from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSPickUpHistoryListRequest,
    WarehouseFBSPickUpHistoryListResponse,
)


class WarehouseFBSPickUpHistoryListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/pickup/history/list"""

    async def warehouse_fbs_pickup_history_list(
            self: "WarehouseFBSPickUpHistoryListMixin",
            request: WarehouseFBSPickUpHistoryListRequest
    ) -> WarehouseFBSPickUpHistoryListResponse:
        """Возвращает историю отгрузок курьерам.

        Notes:
            • Пагинация по `cursor`: передайте полученный `cursor` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpHistoryList

        Args:
            request: Запрос по схеме `WarehouseFBSPickUpHistoryListRequest`

        Returns:
            История отгрузок по схеме `WarehouseFBSPickUpHistoryListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_pickup_history_list(
                    WarehouseFBSPickUpHistoryListRequest(limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/history/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSPickUpHistoryListResponse(**response)
