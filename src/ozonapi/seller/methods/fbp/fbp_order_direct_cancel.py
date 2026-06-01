from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDirectCancelRequest,
    FbpOrderDirectCancelResponse,
)


class FbpOrderDirectCancelMixin(APIManager):
    """Реализует метод /v1/fbp/order/direct/cancel"""

    async def fbp_order_direct_cancel(
            self: "FbpOrderDirectCancelMixin",
            request: FbpOrderDirectCancelRequest,
    ) -> FbpOrderDirectCancelResponse:
        """Отменяет поставку (direct).

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderDirectCancel

        Args:
            request: Идентификатор поставки по схеме `FbpOrderDirectCancelRequest`

        Returns:
            Результат отмены по схеме `FbpOrderDirectCancelResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_direct_cancel(
                    FbpOrderDirectCancelRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/cancel",
            payload=request.model_dump(),
        )
        return FbpOrderDirectCancelResponse(**response)
