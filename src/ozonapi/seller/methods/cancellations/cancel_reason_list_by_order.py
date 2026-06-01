from ...core import APIManager
from ...schemas.cancellations import (
    CancelReasonListByOrderRequest,
    CancelReasonListByOrderResponse,
)


class CancelReasonListByOrderMixin(APIManager):
    """Реализует метод /v1/cancel-reason/list-by-order"""

    async def cancel_reason_list_by_order(
            self: "CancelReasonListByOrderMixin",
            request: CancelReasonListByOrderRequest,
    ) -> CancelReasonListByOrderResponse:
        """Получает динамический список причин отмены для заказа.

        Notes:
            • Возвращает причины отмены, доступные для конкретного заказа.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancelReasonListByOrder

        Args:
            request: Номер заказа по схеме `CancelReasonListByOrderRequest`

        Returns:
            Список причин отмены по схеме `CancelReasonListByOrderResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cancel_reason_list_by_order(
                    CancelReasonListByOrderRequest(order_number="12345678")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list-by-order",
            payload=request.model_dump(),
        )
        return CancelReasonListByOrderResponse(**response)
