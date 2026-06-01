from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSPickUpCourierCancelRequest,
    WarehouseFBSPickUpCourierCancelResponse,
)


class WarehouseFBSPickUpCourierCancelMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/pickup/courier/cancel"""

    async def warehouse_fbs_pickup_courier_cancel(
            self: "WarehouseFBSPickUpCourierCancelMixin",
            request: WarehouseFBSPickUpCourierCancelRequest
    ) -> WarehouseFBSPickUpCourierCancelResponse:
        """Отменяет вызов курьера на забор отгрузки pick-up.

        Notes:
            • Тело ответа отсутствует — успешная отмена подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpCourierCancel

        Args:
            request: Запрос по схеме `WarehouseFBSPickUpCourierCancelRequest`

        Returns:
            Пустой ответ по схеме `WarehouseFBSPickUpCourierCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                await api.warehouse_fbs_pickup_courier_cancel(
                    WarehouseFBSPickUpCourierCancelRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/courier/cancel",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSPickUpCourierCancelResponse(**response)
