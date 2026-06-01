from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSCreateDropOffTimeslotListRequest,
    WarehouseFBSCreateDropOffTimeslotListResponse,
)


class WarehouseFBSCreateDropOffTimeslotListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/create/drop-off/timeslot/list"""

    async def warehouse_fbs_create_drop_off_timeslot_list(
            self: "WarehouseFBSCreateDropOffTimeslotListMixin",
            request: WarehouseFBSCreateDropOffTimeslotListRequest
    ) -> WarehouseFBSCreateDropOffTimeslotListResponse:
        """Возвращает таймслоты отгрузки drop-off для создания склада FBS.

        Notes:
            • `drop_off_point_id` получите методом `warehouse_fbs_create_drop_off_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsCreateDropOffTimeslotList

        Args:
            request: Запрос по схеме `WarehouseFBSCreateDropOffTimeslotListRequest`

        Returns:
            Список таймслотов по схеме `WarehouseFBSCreateDropOffTimeslotListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_create_drop_off_timeslot_list(
                    WarehouseFBSCreateDropOffTimeslotListRequest(drop_off_point_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/drop-off/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSCreateDropOffTimeslotListResponse(**response)
