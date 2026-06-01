from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSCreateDropOffListRequest,
    WarehouseFBSCreateDropOffListResponse,
)


class WarehouseFBSCreateDropOffListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/create/drop-off/list"""

    async def warehouse_fbs_create_drop_off_list(
            self: "WarehouseFBSCreateDropOffListMixin",
            request: WarehouseFBSCreateDropOffListRequest
    ) -> WarehouseFBSCreateDropOffListResponse:
        """Возвращает список drop-off пунктов для создания склада FBS.

        Notes:
            • Используйте полученный `id` пункта при создании склада методом
              `warehouse_fbs_create()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse

        Args:
            request: Запрос по схеме `WarehouseFBSCreateDropOffListRequest`

        Returns:
            Список drop-off пунктов по схеме `WarehouseFBSCreateDropOffListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_create_drop_off_list(
                    WarehouseFBSCreateDropOffListRequest(country_code="RU")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/drop-off/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSCreateDropOffListResponse(**response)
