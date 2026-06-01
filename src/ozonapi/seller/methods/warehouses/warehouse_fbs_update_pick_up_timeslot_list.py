from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSUpdatePickUpTimeslotListRequest,
    WarehouseFBSUpdatePickUpTimeslotListResponse,
)


class WarehouseFBSUpdatePickUpTimeslotListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/update/pick-up/timeslot/list"""

    async def warehouse_fbs_update_pick_up_timeslot_list(
            self: "WarehouseFBSUpdatePickUpTimeslotListMixin",
            request: WarehouseFBSUpdatePickUpTimeslotListRequest
    ) -> WarehouseFBSUpdatePickUpTimeslotListResponse:
        """Возвращает таймслоты отгрузки pick-up для обновления склада FBS.

        Notes:
            • Используйте полученный `id` таймслота при обновлении первой мили
              склада методом `warehouse_fbs_first_mile_update()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsUpdatePickUpTimeslotList

        Args:
            request: Запрос по схеме `WarehouseFBSUpdatePickUpTimeslotListRequest`

        Returns:
            Список таймслотов по схеме `WarehouseFBSUpdatePickUpTimeslotListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_update_pick_up_timeslot_list(
                    WarehouseFBSUpdatePickUpTimeslotListRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/pick-up/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSUpdatePickUpTimeslotListResponse(**response)
