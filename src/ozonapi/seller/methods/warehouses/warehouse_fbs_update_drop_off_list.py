from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSUpdateDropOffListRequest,
    WarehouseFBSUpdateDropOffListResponse,
)


class WarehouseFBSUpdateDropOffListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/update/drop-off/list"""

    async def warehouse_fbs_update_drop_off_list(
            self: "WarehouseFBSUpdateDropOffListMixin",
            request: WarehouseFBSUpdateDropOffListRequest
    ) -> WarehouseFBSUpdateDropOffListResponse:
        """Возвращает список drop-off пунктов для изменения склада FBS.

        Notes:
            • Используйте полученный `id` пункта при обновлении первой мили склада
              методом `warehouse_fbs_first_mile_update()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_ListDropOffPointsForUpdateFBSWarehouse

        Args:
            request: Запрос по схеме `WarehouseFBSUpdateDropOffListRequest`

        Returns:
            Список drop-off пунктов по схеме `WarehouseFBSUpdateDropOffListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_update_drop_off_list(
                    WarehouseFBSUpdateDropOffListRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/drop-off/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSUpdateDropOffListResponse(**response)
