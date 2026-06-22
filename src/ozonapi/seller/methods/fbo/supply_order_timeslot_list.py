from ...core import APIManager
from ...schemas.fbo import SupplyOrderTimeslotListRequest, SupplyOrderTimeslotListResponse


class SupplyOrderTimeslotListMixin(APIManager):
    """Реализует метод /v2/supply-order/timeslot/list"""

    async def supply_order_timeslot_list(
            self: "SupplyOrderTimeslotListMixin",
            request: SupplyOrderTimeslotListRequest
    ) -> SupplyOrderTimeslotListResponse:
        """Метод для получения списка доступных интервалов поставки заявки.

        Notes:
            • Возвращает список доступных интервалов поставки по местному времени склада.
            • Дополнительно возвращает ограничения на изменение интервала и причины,
              по которым изменить интервал нельзя.
            • Выбранный интервал устанавливают методом `supply_order_timeslot_update`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderTimeslotList

        Args:
            request: Запрос на получение интервалов поставки по схеме `SupplyOrderTimeslotListRequest`

        Returns:
            Доступные интервалы поставки по схеме `SupplyOrderTimeslotListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_timeslot_list(
                    SupplyOrderTimeslotListRequest(order_id=1234567890)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="supply-order/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderTimeslotListResponse(**response)
