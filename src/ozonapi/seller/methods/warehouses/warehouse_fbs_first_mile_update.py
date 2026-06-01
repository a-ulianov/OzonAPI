from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSFirstMileUpdateRequest,
    WarehouseFBSFirstMileUpdateResponse,
)


class WarehouseFBSFirstMileUpdateMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/first-mile/update"""

    async def warehouse_fbs_first_mile_update(
            self: "WarehouseFBSFirstMileUpdateMixin",
            request: WarehouseFBSFirstMileUpdateRequest
    ) -> WarehouseFBSFirstMileUpdateResponse:
        """Обновляет настройки первой мили склада FBS.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/UpdateWarehouseFBSFirstMile

        Args:
            request: Запрос по схеме `WarehouseFBSFirstMileUpdateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseFBSFirstMileUpdateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_first_mile_update(
                    WarehouseFBSFirstMileUpdateRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/first-mile/update",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSFirstMileUpdateResponse(**response)
