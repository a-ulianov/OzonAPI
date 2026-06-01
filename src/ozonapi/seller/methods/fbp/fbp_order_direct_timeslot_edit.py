from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDirectTimeslotEditRequest,
    FbpOrderDirectTimeslotEditResponse,
)


class FbpOrderDirectTimeslotEditMixin(APIManager):
    """Реализует метод /v1/fbp/order/direct/timeslot/edit"""

    async def fbp_order_direct_timeslot_edit(
            self: "FbpOrderDirectTimeslotEditMixin",
            request: FbpOrderDirectTimeslotEditRequest,
    ) -> FbpOrderDirectTimeslotEditResponse:
        """Редактирует таймслот в заявке на поставку.

        Notes:
            • При ошибке брони таймслота заполняется `error_reasons`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpEditTimeslot

        Args:
            request: Параметры изменения таймслота по схеме
                `FbpOrderDirectTimeslotEditRequest`

        Returns:
            Результат изменения по схеме `FbpOrderDirectTimeslotEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_direct_timeslot_edit(
                    FbpOrderDirectTimeslotEditRequest(
                        supply_id="70",
                        row_version=1,
                        timeslot_start="2026-06-11T10:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/timeslot/edit",
            payload=request.model_dump(),
        )
        return FbpOrderDirectTimeslotEditResponse(**response)
