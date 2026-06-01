from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSUpdateDropOffTimeslotListRequest,
    WarehouseFBSUpdateDropOffTimeslotListResponse,
)


class WarehouseFBSUpdateDropOffTimeslotListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/update/drop-off/timeslot/list"""

    async def warehouse_fbs_update_drop_off_timeslot_list(
            self: "WarehouseFBSUpdateDropOffTimeslotListMixin",
            request: WarehouseFBSUpdateDropOffTimeslotListRequest
    ) -> WarehouseFBSUpdateDropOffTimeslotListResponse:
        """Возвращает таймслоты отгрузки drop-off для обновления склада FBS.

        Notes:
            • `drop_off_point_id` получите методом `warehouse_fbs_update_drop_off_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsUpdateDropOffTimeslotList

        Args:
            request: Запрос по схеме `WarehouseFBSUpdateDropOffTimeslotListRequest`

        Returns:
            Список таймслотов по схеме `WarehouseFBSUpdateDropOffTimeslotListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_update_drop_off_timeslot_list(
                    WarehouseFBSUpdateDropOffTimeslotListRequest(
                        drop_off_point_id=123, warehouse_id=456
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/drop-off/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSUpdateDropOffTimeslotListResponse(**response)
