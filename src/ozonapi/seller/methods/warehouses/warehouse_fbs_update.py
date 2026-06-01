from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSUpdateRequest,
    WarehouseFBSUpdateResponse,
)


class WarehouseFBSUpdateMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/update"""

    async def warehouse_fbs_update(
            self: "WarehouseFBSUpdateMixin",
            request: WarehouseFBSUpdateRequest
    ) -> WarehouseFBSUpdateResponse:
        """Обновляет данные склада FBS.

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.
            • Настройки первой мили обновляются отдельным методом
              `warehouse_fbs_first_mile_update()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/UpdateWarehouseFBS

        Args:
            request: Запрос обновления склада по схеме `WarehouseFBSUpdateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseFBSUpdateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_update(
                    WarehouseFBSUpdateRequest(warehouse_id=123, name="Новое имя")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSUpdateResponse(**response)
