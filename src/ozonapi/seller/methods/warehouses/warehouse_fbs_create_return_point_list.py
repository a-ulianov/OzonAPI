from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSCreateReturnPointListRequest,
    WarehouseFBSCreateReturnPointListResponse,
)


class WarehouseFBSCreateReturnPointListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/create/return-point/list"""

    async def warehouse_fbs_create_return_point_list(
            self: "WarehouseFBSCreateReturnPointListMixin",
            request: WarehouseFBSCreateReturnPointListRequest
    ) -> WarehouseFBSCreateReturnPointListResponse:
        """Возвращает список пунктов возврата для создания склада FBS.

        Notes:
            • Пагинация по `last_id`: при `has_next` равном true передайте полученный
              `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFBSCreateReturnPointList

        Args:
            request: Запрос по схеме `WarehouseFBSCreateReturnPointListRequest`

        Returns:
            Список пунктов возврата по схеме `WarehouseFBSCreateReturnPointListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_create_return_point_list(
                    WarehouseFBSCreateReturnPointListRequest(country_code="RU", limit=20)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/return-point/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSCreateReturnPointListResponse(**response)
