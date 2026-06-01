from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderPickUpCancelRequest,
    FbpOrderPickUpCancelResponse,
)


class FbpOrderPickUpCancelMixin(APIManager):
    """Реализует метод /v1/fbp/order/pick-up/cancel"""

    async def fbp_order_pick_up_cancel(
            self: "FbpOrderPickUpCancelMixin",
            request: FbpOrderPickUpCancelRequest,
    ) -> FbpOrderPickUpCancelResponse:
        """Отменяет pick-up поставку.

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderPickUpCancel

        Args:
            request: Идентификатор поставки по схеме `FbpOrderPickUpCancelRequest`

        Returns:
            Результат отмены по схеме `FbpOrderPickUpCancelResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_pick_up_cancel(
                    FbpOrderPickUpCancelRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/pick-up/cancel",
            payload=request.model_dump(),
        )
        return FbpOrderPickUpCancelResponse(**response)
