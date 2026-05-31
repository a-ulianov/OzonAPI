from ...core import APIManager
from ...schemas.fbo import SupplyOrderTimeslotUpdateRequest, SupplyOrderTimeslotUpdateResponse


class SupplyOrderTimeslotUpdateMixin(APIManager):
    """Реализует метод /v1/supply-order/timeslot/update"""

    async def supply_order_timeslot_update(
            self: "SupplyOrderTimeslotUpdateMixin",
            request: SupplyOrderTimeslotUpdateRequest
    ) -> SupplyOrderTimeslotUpdateResponse:
        """Метод для обновления интервала поставки заявки.

        Notes:
            • Операция асинхронная: метод возвращает `operation_id`, статус выполнения
              проверяйте методом `supply_order_timeslot_status`.
            • Доступные интервалы получают методом `supply_order_timeslot_get`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_UpdateSupplyOrderTimeslot

        Args:
            request: Запрос на обновление интервала поставки по схеме `SupplyOrderTimeslotUpdateRequest`

        Returns:
            Идентификатор операции обновления по схеме `SupplyOrderTimeslotUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_timeslot_update(
                    SupplyOrderTimeslotUpdateRequest(
                        supply_order_id=1234567890,
                        timeslot=SupplyOrderTimeslot(
                            from_=datetime.datetime(2026, 6, 1, 10, 0),
                            to=datetime.datetime(2026, 6, 1, 12, 0),
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/update",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderTimeslotUpdateResponse(**response)
