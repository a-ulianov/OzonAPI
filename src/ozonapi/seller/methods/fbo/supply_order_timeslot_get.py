from ...core import APIManager
from ...schemas.fbo import SupplyOrderTimeslotGetRequest, SupplyOrderTimeslotGetResponse


class SupplyOrderTimeslotGetMixin(APIManager):
    """Реализует метод /v1/supply-order/timeslot/get"""

    async def supply_order_timeslot_get(
            self: "SupplyOrderTimeslotGetMixin",
            request: SupplyOrderTimeslotGetRequest
    ) -> SupplyOrderTimeslotGetResponse:
        """Метод для получения доступных интервалов поставки заявки.

        Notes:
            • Возвращает список доступных интервалов поставки по местному времени склада.
            • Выбранный интервал устанавливают методом `supply_order_timeslot_update`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderTimeslots

        Args:
            request: Запрос на получение интервалов поставки по схеме `SupplyOrderTimeslotGetRequest`

        Returns:
            Доступные интервалы поставки по схеме `SupplyOrderTimeslotGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_timeslot_get(
                    SupplyOrderTimeslotGetRequest(supply_order_id=1234567890)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/get",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderTimeslotGetResponse(**response)
