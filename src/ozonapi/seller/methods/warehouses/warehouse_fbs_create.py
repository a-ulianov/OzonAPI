from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSCreateRequest,
    WarehouseFBSCreateResponse,
)


class WarehouseFBSCreateMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/create"""

    async def warehouse_fbs_create(
            self: "WarehouseFBSCreateMixin",
            request: WarehouseFBSCreateRequest
    ) -> WarehouseFBSCreateResponse:
        """Создаёт склад FBS.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.
            • `drop_off_point_id` и `timeslot_id` получите методами списков
              `warehouse_fbs_create_drop_off_list()` и
              `warehouse_fbs_create_drop_off_timeslot_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_CreateWarehouseFBS

        Args:
            request: Запрос создания склада по схеме `WarehouseFBSCreateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseFBSCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_create(
                    WarehouseFBSCreateRequest(name="Склад", phone="+70000000000")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSCreateResponse(**response)
