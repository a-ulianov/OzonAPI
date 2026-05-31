from ...core import APIManager
from ...schemas.fbo import SupplyOrderTimeslotStatusRequest, SupplyOrderTimeslotStatusResponse


class SupplyOrderTimeslotStatusMixin(APIManager):
    """Реализует метод /v1/supply-order/timeslot/status"""

    async def supply_order_timeslot_status(
            self: "SupplyOrderTimeslotStatusMixin",
            request: SupplyOrderTimeslotStatusRequest
    ) -> SupplyOrderTimeslotStatusResponse:
        """Метод для получения статуса обновления интервала поставки.

        Notes:
            • Используется вместе с `supply_order_timeslot_update`: передайте полученный
              `operation_id` для проверки результата операции.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderTimeslotStatus

        Args:
            request: Запрос на получение статуса обновления по схеме `SupplyOrderTimeslotStatusRequest`

        Returns:
            Статус обновления интервала поставки по схеме `SupplyOrderTimeslotStatusResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_timeslot_status(
                    SupplyOrderTimeslotStatusRequest(operation_id="operation-id")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/status",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderTimeslotStatusResponse(**response)
