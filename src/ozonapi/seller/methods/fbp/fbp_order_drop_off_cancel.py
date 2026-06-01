from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDropOffCancelRequest,
    FbpOrderDropOffCancelResponse,
)


class FbpOrderDropOffCancelMixin(APIManager):
    """Реализует метод /v1/fbp/order/drop-off/cancel"""

    async def fbp_order_drop_off_cancel(
            self: "FbpOrderDropOffCancelMixin",
            request: FbpOrderDropOffCancelRequest,
    ) -> FbpOrderDropOffCancelResponse:
        """Отменяет поставку drop-off.

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderDropOffCancel

        Args:
            request: Идентификатор поставки по схеме `FbpOrderDropOffCancelRequest`

        Returns:
            Результат отмены по схеме `FbpOrderDropOffCancelResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_drop_off_cancel(
                    FbpOrderDropOffCancelRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/cancel",
            payload=request.model_dump(),
        )
        return FbpOrderDropOffCancelResponse(**response)
