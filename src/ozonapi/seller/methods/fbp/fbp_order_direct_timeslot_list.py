from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDirectTimeslotListRequest,
    FbpOrderDirectTimeslotListResponse,
)


class FbpOrderDirectTimeslotListMixin(APIManager):
    """Реализует метод /v1/fbp/order/direct/timeslot/list"""

    async def fbp_order_direct_timeslot_list(
            self: "FbpOrderDirectTimeslotListMixin",
            request: FbpOrderDirectTimeslotListRequest,
    ) -> FbpOrderDirectTimeslotListResponse:
        """Получает список таймслотов для поставки.

        Notes:
            • Возвращает доступные таймслоты в заданном интервале и часовой пояс склада.
            • Если таймслотов нет, заполняется `reasons` с причинами.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpAvailableTimeslotList

        Args:
            request: Параметры поиска таймслотов по схеме
                `FbpOrderDirectTimeslotListRequest`

        Returns:
            Список таймслотов по схеме `FbpOrderDirectTimeslotListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_direct_timeslot_list(
                    FbpOrderDirectTimeslotListRequest(
                        supply_id="70",
                        interval_start="2026-06-10T00:00:00Z",
                        interval_end="2026-06-12T00:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/timeslot/list",
            payload=request.model_dump(),
        )
        return FbpOrderDirectTimeslotListResponse(**response)
