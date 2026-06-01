from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSUpdateReturnPointListRequest,
    WarehouseFBSUpdateReturnPointListResponse,
)


class WarehouseFBSUpdateReturnPointListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/update/return-point/list"""

    async def warehouse_fbs_update_return_point_list(
            self: "WarehouseFBSUpdateReturnPointListMixin",
            request: WarehouseFBSUpdateReturnPointListRequest
    ) -> WarehouseFBSUpdateReturnPointListResponse:
        """Возвращает список пунктов возврата для обновления склада FBS.

        Notes:
            • Пагинация по `last_id`: при `has_next` равном true передайте полученный
              `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFBSUpdateReturnPointList

        Args:
            request: Запрос по схеме `WarehouseFBSUpdateReturnPointListRequest`

        Returns:
            Список пунктов возврата по схеме `WarehouseFBSUpdateReturnPointListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_update_return_point_list(
                    WarehouseFBSUpdateReturnPointListRequest(warehouse_id=123, limit=20)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/return-point/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSUpdateReturnPointListResponse(**response)
