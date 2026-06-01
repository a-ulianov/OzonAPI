from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSCreatePickUpTimeslotListRequest,
    WarehouseFBSCreatePickUpTimeslotListResponse,
)


class WarehouseFBSCreatePickUpTimeslotListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/create/pick-up/timeslot/list"""

    async def warehouse_fbs_create_pick_up_timeslot_list(
            self: "WarehouseFBSCreatePickUpTimeslotListMixin",
            request: WarehouseFBSCreatePickUpTimeslotListRequest
    ) -> WarehouseFBSCreatePickUpTimeslotListResponse:
        """Возвращает таймслоты отгрузки pick-up для создания склада FBS.

        Notes:
            • `is_pickup_supported` равно false, если по адресу отгрузка pick-up
              недоступна.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsCreatePickUpTimeslotList

        Args:
            request: Запрос по схеме `WarehouseFBSCreatePickUpTimeslotListRequest`

        Returns:
            Список таймслотов по схеме `WarehouseFBSCreatePickUpTimeslotListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_create_pick_up_timeslot_list(
                    WarehouseFBSCreatePickUpTimeslotListRequest(is_kgt=False)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/pick-up/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSCreatePickUpTimeslotListResponse(**response)
