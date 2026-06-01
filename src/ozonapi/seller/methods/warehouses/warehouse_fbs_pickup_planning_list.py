from ...core import APIManager
from ...schemas.warehouses import WarehouseFBSPickUpPlanningListResponse


class WarehouseFBSPickUpPlanningListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/pickup/planning/list"""

    async def warehouse_fbs_pickup_planning_list(
            self: "WarehouseFBSPickUpPlanningListMixin"
    ) -> WarehouseFBSPickUpPlanningListResponse:
        """Возвращает список складов для планирования отгрузок курьеру.

        Notes:
            • Запрос без тела.
            • Запланировать отгрузку можно, если `can_modify_pickup_plan` равно true.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpPlanningList

        Returns:
            Список складов по схеме `WarehouseFBSPickUpPlanningListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_pickup_planning_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/planning/list",
            payload={}
        )
        return WarehouseFBSPickUpPlanningListResponse(**response)
